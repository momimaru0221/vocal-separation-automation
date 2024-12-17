## タイトル (Conventional Commits 準拠)

- タイトル例: `feat: add new endpoint for user data`
- 必ず `feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, `perf:`, `test:` などのプリフィックスを使用してください。
- タイトルは変更内容を的確に表現してください。

## 説明

- 変更点の概要: このPRで追加/修正した機能やコード箇所を簡潔に説明
- 背景/目的: なぜこの変更が必要なのか、どの問題を解決するのか

## ラベル付与（patch/minor/major）

- この変更が次回リリースでどのようなバージョンアップを伴うか、適切なラベルをPRに付与してください。
  - `patch`: バグ修正や小さな改善
  - `minor`: 後方互換性を保った新機能追加
  - `major`: 後方互換性を壊す変更（Breaking Change）

**手順**:
1. PRを作成する際、このテンプレートが自動的に反映されます。
2. PR作成画面でタイトルをConventional Commits準拠で編集。
3. 説明欄に変更点・背景を追記。
4. 右側の「Labels」から`patch`, `minor`, `major`のいずれかを選択。

これにより、semantic-releaseは、
- CommitsおよびPRタイトルのフォーマットからリリースノートを生成。
- `patch`, `minor`, `major`のラベルから次バージョンを自動計算する。

### 2. CIによるバリデーション (任意)

`pull_request`イベントをトリガーとしてGitHub Actionsを設定し、PRタイトルやコミットメッセージがConventional Commitsに準拠しているかをチェックすることも可能。

**例： `.github/workflows/pr-validation.yml`**

```yaml
name: PR Validation
on:
  pull_request:
    types: [opened, edited, synchronize]

jobs:
  conventional-commit-check:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Check PR Title
        run: |
          # PRタイトルを取得
          TITLE=$(jq -r '.pull_request.title' $GITHUB_EVENT_PATH)
          # シンプルな正規表現チェック例（"type: description"形式になっているか）
          if [[ ! $TITLE =~ ^(feat|fix|chore|docs|refactor|perf|test): ]]; then
            echo "PR title does not follow Conventional Commits."
            exit 1
          fi
      # ここでさらにcommitlintを走らせてコミットメッセージ検証も可能
