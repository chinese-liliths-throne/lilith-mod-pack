from pathlib import Path
from typing import Dict, List

README_HEAD = [
	"# lilith-mod-pack\n",
	"A repo to collect interesting Lilith's Throme mods.\n"
]

path = Path('./')
mod_list : Dict[str, List[str]] = {}

for dir in path.iterdir():
	if dir.is_dir() and dir.name != ".git":
		name = dir.name
		author_name = filter(lambda x : x.is_dir(),list(dir.iterdir())).__next__().name
		if mod_list.get(author_name) is None:
			mod_list[author_name] = [name]
		else:
			mod_list[author_name].append(name)

mod_list = dict(sorted(mod_list.items(), key=lambda item: item[0]))

markdown = []

for (author, mods) in mod_list.items():
	li = f" - {author}\n"
	for mod in mods:
		li += f"   1. [{mod}](/{mod})\n"
	markdown.append(li)

readme = README_HEAD + ["## Mod List\n"] + markdown 

with open("./README.md", "w", encoding="utf-8") as f:
	f.writelines(readme)