# Scriptorium

짧은 글·기고문·노트를 Markdown으로 쓰고, [md2hwp](https://github.com/esnahn/md2hwp)로 최종 원고를 HWP로 변환하는 작업 저장소다.

## 파일

- `title.md`: 제목 후보를 나열하고 최종안을 정한다.
- `outline.md`: 목차와 섹션별 핵심 내용을 정리한다.
- `draft.md`: 원고. 항상 **한 편만** 다루며, md2hwp 원고 문법으로 쓴다.
- `instruction_writing.md`: 표기법·참고문헌 규칙.
- `references/`: 참고 보고서, 메모, 통계 등.
- `scripts/count_words.py`: 원고 분량(글자 수, 단어 수) 측정. Python 3 표준 라이브러리만 쓰므로 가상환경이나 패키지 설치는 필요 없다.
- `md2hwp/`: 변환기. git에서 제외되며 아래 명령으로 받는다.

## 작업 흐름

1. `title.md`에 제목 후보를 적고 고른다.
2. `outline.md`로 뼈대를 잡는다.
3. `draft.md`에 본문을 쓴다. `references/`의 자료를 활용한다.
4. 검사하고 HWP로 변환한다(아래).
5. 분량을 확인한다.
   - 집필 중: `python scripts/count_words.py draft.md`. 마크다운 기호(`#`, `|`, `**`, YAML 머리말 등)까지 세므로 실제보다 조금 많게 나온다.
   - 최종본: 변환된 HWP를 한글에서 열어 **파일 → 문서 정보 → 문서 통계**로 확인한다.
6. 원고가 끝나면 원고와 자료를 별도 보관 위치로 옮기고, 이 저장소에는 재사용할 템플릿만 남긴다.

## 원고 문법

- Markdown 문법(YAML 제목, 장·절, 표 캡션과 `출처:`, 각주, 수식, 상호참조)은 `md2hwp/README-MANUSCRIPT.md`를 따른다. AI에게 원고를 맡길 때는 `md2hwp/AGENTS.md`를 함께 준다.
- 표기법과 참고문헌 형식은 `instruction_writing.md`를 따른다.

## md2hwp 설치·갱신

저장소 루트에서 실행한다. 최신 릴리스를 받아 `md2hwp/`를 통째로 교체하므로 갱신할 때도 같은 명령을 쓴다([GitHub CLI](https://cli.github.com/) 필요, 없으면 [Releases](https://github.com/esnahn/md2hwp/releases)에서 zip을 받아 `md2hwp/`에 푼다).

```powershell
gh release download -R esnahn/md2hwp -p "*windows-x64.zip" -O md2hwp.zip --clobber
Remove-Item md2hwp -Recurse -ErrorAction Ignore; Expand-Archive md2hwp.zip md2hwp; Remove-Item md2hwp.zip
```

처음 한 번은 Pandoc을 받는다. 사용자 폴더(`%LOCALAPPDATA%\md2hwp`)에 설치되므로 md2hwp를 갱신해도 다시 할 필요가 없다.

```powershell
.\md2hwp\md2hwp.exe setup-pandoc
```

## 검사와 변환

```powershell
.\md2hwp\md2hwp.exe validate draft.md --require-meta title
.\md2hwp\md2hwp.exe draft.md
```

`draft.output.hwp`(최종 원고)와 `draft.ir.json`(중간 파일)이 원고 옆에 생긴다. 둘 다 git에서 제외되며 언제든 다시 만들 수 있다. 변환 뒤에는 한글에서 열어 표·글상자 잘림, 쪽 나눔, 각주 번호를 직접 확인한다.
