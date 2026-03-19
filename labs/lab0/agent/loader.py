"""Load all SKILL.md files from skills subdirectories."""

from pathlib import Path


def load_all_skills(skills_dir: Path = Path("skills")) -> str:
    """Scan skills/*/SKILL.md and skills/*/skill.md, load and merge their content.

    Strips YAML frontmatter from each file. Skips empty files.
    Returns concatenated body content separated by "\\n\\n---\\n\\n".
    """
    skill_contents: list[str] = []

    for path in sorted(skills_dir.iterdir()):
        if not path.is_dir():
            continue
        # Try SKILL.md first, then skill.md
        for name in ("SKILL.md", "skill.md"):
            skill_file = path / name
            if skill_file.exists():
                with open(skill_file, 'r', encoding='utf-8') as f:
                    content = skill_file.read_text(encoding="utf-8").strip()
                    if not content:
                        continue  # 跳过空文件
                    body = strip_yaml(content)
                    skill_contents.append(body)
                    #* only load one successful md
                    break

                #pass # TODO: implement this
    #print ("\n\n---\n\n".join(skill_contents))
    return "\n\n---\n\n".join(skill_contents)

def strip_yaml(text:str) -> str:
    lines = text.splitlines()
    if lines and lines[0] == "---":
        for i in range (1, len(lines)):
            if lines[i] == "---":
                return "\n".join(lines[i+1:]).lstrip() # do a slide and leftstrip
            #TODO robust
        return ""
    return text