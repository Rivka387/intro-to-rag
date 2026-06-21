import json
from pathlib import Path


def main() -> None:
    notebook_path = Path("intro_to_rag.ipynb")
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    env: dict[str, object] = {"__name__": "__main__"}

    for index, cell in enumerate(notebook["cells"], start=1):
        if cell.get("cell_type") != "code":
            continue

        source = "".join(cell.get("source", []))
        if not source.strip():
            continue

        print(f"\n=== Running code cell {index} ===")
        exec(compile(source, f"{notebook_path.name}:cell_{index}", "exec"), env, env)


if __name__ == "__main__":
    main()
