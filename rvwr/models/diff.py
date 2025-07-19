from __future__ import annotations

from dataclasses import dataclass, field

from unidiff import PatchSet


@dataclass
class DiffLine:
    line_type: str  # '+', '-', or ' ' for added, removed, unchanged
    content: str
    source_line_no: int | None
    target_line_no: int | None


@dataclass
class DiffFile:
    path: str
    lines: list[DiffLine] = field(default_factory=list)


@dataclass
class Diff:
    files: list[DiffFile] = field(default_factory=list)

    @classmethod
    def from_str(cls, diff_str: str) -> Diff:
        patch = PatchSet(diff_str)

        files = []
        for patched_file in patch:
            diff_lines = []
            for hunk in patched_file:
                for line in hunk:
                    diff_lines.append(
                        DiffLine(
                            line_type=line.line_type,
                            content=line.value.rstrip("\n"),
                            source_line_no=line.source_line_no,
                            target_line_no=line.target_line_no,
                        )
                    )
            files.append(DiffFile(path=patched_file.path, lines=diff_lines))

        return cls(files=files)
