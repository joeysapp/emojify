class Emoji():
    def __init__(self, *args, **kwargs):
        self.emoji = args[0] if args and len(args) > 0 else kwargs.get('emoji') or 'n/a'
        self.derived = []
        self.derived_source = []
        self.description = kwargs.get('description')
        self.tags = kwargs.get('tags')
        self.idx = kwargs.get('idx') or 0
        self.unicode = args[1] if args and len(args) > 1 else kwargs.get('unicode') or b'\\u00000000'
        # self.discord_emoji = ''

    def __repr__(self):
        return "{}".format(self.emoji)

import json
def loadEmojisAsJSON(fname, emojis=[]):
    res = []
    with open(fname) as f:
        f = json.load(f)
        f = f['annotations'] if 'annotations' in f else f['annotationsDerived']
        f = f['annotations']
        idx = 0
        for k in f.keys():
            idx += 1
            description = ''.join(f[k]['tts']) if 'tts' in f[k] else ''
            tags = f[k]['default'] if 'default' in f[k] else []
            e = Emoji(k, unicode=k.encode('unicode_escape'), description=description, tags=tags, idx=idx)
            if not len(emojis):
                res.append(e)
            else:
                starting_desc_idx = description.find(':') # e.g. 'woman astronaut: medium-light skin tone'
                starting_desc = description[0:starting_desc_idx]
                for starting_emoji in emojis:
                    if starting_emoji.description == starting_desc:
                        e.derived_source = starting_emoji
                        starting_emoji.derived.append(e)
                        res.append(e)
                        continue
    return res

def sortEmojis(emojis):
    return sorted(emojis, key=lambda emoji: emoji.description)

def initEmojis():
    e = loadEmojisAsJSON('src/annotations-full.json')
    # Note Derivations include things like flags, numbers
    e_d = loadEmojisAsJSON('src/annotations-derived-full.json', emojis)
    return [sortEmojis(e), sortEmojis(e_d)]

[emojis, emojis_derived] = initEmojis()
