import markdown


class TLabel:
    def __init__(self, board, data):
        self.board = board
        self.name = data.get('name')
        self.id = data.get('id')
        self.uses = data.get('uses')
        self.color = data.get('color')

    @property
    def cards(self):
        result = []
        for card in self.board.cards:
            for label in card._labels:
                if label.get('id') == self.id:
                    result.append(card)

        return result


class TList:
    def __init__(self, board, payload):
        self.board = board
        self.name = payload.get('name')
        self.id = payload.get('id')

    @property
    def cards(self):
        result = []
        for card in self.board.cards:
            if card.list_id == self.id:
                result.append(card)

        return result


class TCard:
    def __init__(self, board, data):
        self.board = board
        self._labels = data.get('labels')
        self.list_id = data.get('idList')
        self.name = data.get('name')
        self.desc = data.get('desc')
        self.previews = [TPreview(preview) for attachment in data.get('attachments') for preview in
                         attachment.get('previews')]

        try:
            self.src = data['attachments'][0]['url']
        except Exception:
            self.src = ''

    @property
    def description_html(self):
        return markdown.markdown(self.desc)

    @property
    def list(self):
        for _list in self.board.lists:
            if _list.id == self.list_id:
                return _list

    @property
    def labels(self):
        result = []
        label_ids = [l['id'] for l in self._labels]
        for label in self.board.labels:
            if label.id in label_ids:
                result.append(label)

        return result


class TBoard:
    def __init__(self, data):
        _labels = data.get('labels')
        _cards = data.get('cards')
        _lists = data.get('lists')

        self.name = data.get('name')
        self.desc = data.get('desc')
        self.id = data.get('id')

        self.cards = [TCard(self, card) for card in _cards]
        self.labels = [TLabel(self, label) for label in _labels if label.get('name')]
        self.lists = [TList(self, _list) for _list in _lists if not _list.get("closed")]

    def get_label_by_id(self, id):
        for label in self.labels:
            if label.id == id:
                return label
        return None

    def get_list_by_id(self, id):
        for lst in self.lists:
            if lst.id == id:
                return lst
        return None


class TPreview:
    def __init__(self, data):
        self.bytes = data.get("bytes")
        self.url = data.get("url")
        self.width = data.get("width")
        self.height = data.get("height")
        self.scaled = data.get("scaled")
