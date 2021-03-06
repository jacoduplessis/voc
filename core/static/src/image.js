function getCSRF () {
  const el = document.querySelector('input[name="csrfmiddlewaretoken"]')
  if (!el) return null
  return el.value
}

const app = new Vue({
  name: 'BulkImageUploader',
  template: `
    <div>
        
        <p>
          <label for="tags">Tags</label>
          <input v-model="tags" name="tags" placeholder="">
          <div class="help">Comma-seperated list without underscores and whitespace</div>
        </p>
        
        <input multiple type="file" @change="onChange" accept="image/*">
        <div class="help">Upload will start as soon as files are selected</div>
        <div v-for="image in images" style="border: 2px solid #aaa; padding: 1rem">
             
            <img :src="image.src" style="max-width: 200px">
            <p>{{image.file.name}} <strong>{{(image.file.size/1000000).toFixed(2)}}MB</strong></p>
            <p v-if="image.message" :style="{backgroundColor: image.uploaded ? 'green' : 'red'}" style="color: white; padding: 0.5rem 1rem">{{image.message}}</p>
        </div>
    </div>
`,
  data: {
    images: [],
    tags: '',
  },
  methods: {

    onChange(e) {

      Array.from(e.target.files).forEach(f => {

        let image = {}
        let ix = null
        const reader = new FileReader();

        reader.readAsDataURL(f)
        reader.onload = (e) => {
          image.src = e.target.result
          image.file = f
          ix = this.images.unshift(image) - 1
        }

        const formData = new FormData();
        formData.append('image', f);
        formData.append('tags', this.tags)

        fetch(window.location, {
          method: 'POST',
          headers: {
            'X-CSRFToken': getCSRF(),
          },
          credentials: 'include',
          body: formData,
        }).then(r => r.json()).then(data => {
          image.uploaded = data.ok
          image.message = data.ok ? 'Upload successful' : JSON.stringify(data.errors)
          image.id = data.id
          this.$set(this.images, ix, image)
        }).catch(err => {
          image.uploaded = false
          image.message = err
          this.$set(this.images, ix, image)
        })

      })


    }
  }
})

app.$mount('#app')