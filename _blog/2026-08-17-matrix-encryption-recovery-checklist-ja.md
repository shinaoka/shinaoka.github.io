---
layout: single
title: "既存Matrix利用者の暗号化設定・安全な回復チェックリスト"
date: 2026-08-17
lang: ja
excerpt: "すでにMatrixを使っている人が、現在の復号鍵を失わずに端末検証、Secure Backup、リカバリーキーを整えるための分岐付き手順です。"
permalink: /blog/matrix-encryption-safety-recovery-checklist-ja/
toc: true
toc_label: "目次"
---

**言語:** 日本語 / [English](/blog/matrix-encryption-safety-recovery-checklist/)

**対象者:** [初めて使う人](/blog/matrix-encryption-setup-checklist-ja/) / **すでに使っている人**

<div class="notice--danger" markdown="1">
## 確認が終わるまで、現在ログインしている端末を失わないでください

ログアウト、アプリの削除・再インストール、ブラウザーのサイトデータ削除、セッション削除、Secure BackupやデジタルIDのリセットを行わないでください。今読めている端末だけが、まだバックアップされていない復号鍵を持っている可能性があります。
</div>

## 最初に確認する完了条件

- [ ] ログイン済みの検証済み端末が1台以上ある
- [ ] Secure Backupが有効である
- [ ] 有効なリカバリーキーを安全な場所に保存した
- [ ] スマートフォンではElement Xへログインし、検証を完了した
- [ ] 2台以上の端末で過去の暗号化メッセージを読める

## 1. 現在の端末を棚卸しする

- [ ] [Element WebのSessions画面](https://app.element.io/#/settings/sessions)を開く
- [ ] **Current Session**の緑の盾を確認する
- [ ] **Other Sessions → Verified: Ready for secure messaging**を確認する
- [ ] **Unverified: Not ready for secure messaging**にある使用中の端末を記録する

直接リンクが開かない場合は、Element Web/Desktopで **プロフィール画像 → All Settings → Sessions** と進みます。

`account.matrix.org`の端末一覧はログインセッションの管理用です。暗号学的に検証済みかどうかは、ElementのSessions画面の緑の盾またはVerifiedフィルターで判断してください。同じPCでも、ブラウザー、Element Desktop、Koushiは別端末です。

### 次に進む分岐

1. **検証済み端末がある** → [2A](#2a-検証済み端末がある)
2. **検証済み端末はないが、過去を読めるElement Web/Desktopがある** → [2B](#2b-検証済み端末がないが過去を読める)
3. **リカバリーキーも、検証済み端末も、過去を読める端末もない** → [2C](#2c-回復手段が残っていない)

## 2A. 検証済み端末がある

- [ ] 過去のメッセージを読める検証済み端末を「基準端末」に決め、作業中はログアウトしない
- [ ] 基準端末で **Settings → Encryption**を開く
- [ ] **Get recovery key**なら、案内に従ってSecure Backupとキーを設定する
- [ ] **Change recovery key**だが現在のキーがない場合、新しいリカバリーキーへ変更する
- [ ] 新しいキーを安全な場所へ保存する
- [ ] Secure Backupが有効で、バックアップが動作していることを確認する
- [ ] 他の端末へリカバリーキーを入力し、検証する
- [ ] 各端末で過去の暗号化メッセージを読めることを確認する

## 2B. 検証済み端末がないが過去を読める

リセットの前に、読めるElement Web/Desktopが持つ復号鍵を退避します。

- [ ] 読めるElement Web/Desktopをすべて起動したままにする
- [ ] 各端末で **Security & Privacy → Export E2E room keys**を実行する
- [ ] exportファイルごとに強いパスフレーズを設定し、安全に保存する
- [ ] 複数端末がある場合、各端末から別々にexportする
- [ ] exportファイルが実際に保存されたことを確認する

<div class="notice--warning" markdown="1">
**Element XからSecure Backupをリセットしないでください。** Element Xは復号鍵全体のexportに対応しておらず、ローカルにない鍵を失う可能性があります。
</div>

export完了後に限り、Element Web/Desktopで次を実行します。

- [ ] デジタルIDとSecure Backupをリセットする
- [ ] 新しいリカバリーキーを発行し、安全に保存する
- [ ] 基準端末を検証する
- [ ] 保存したすべてのE2E room keyファイルを基準端末へimportする
- [ ] Secure Backupを有効にし、importした鍵がバックアップされるのを待つ
- [ ] 他の端末を検証し、新しいキーを入力する
- [ ] 各端末で過去の暗号化メッセージを確認する

## 2C. 回復手段が残っていない

有効なリカバリーキー、検証済み端末、過去を読めるログイン済み端末がすべてない場合、以前の復号鍵を回収する方法はありません。サービス管理者も復号できません。

- [ ] 過去の暗号化履歴を失う可能性を理解する
- [ ] Element Web/DesktopからデジタルIDをリセットする
- [ ] 新しいリカバリーキーを発行して保存する
- [ ] Secure Backupを有効にする
- [ ] 使用するすべての端末を検証する

## 3. Element Xへ移行する

- [ ] スマートフォンの旧Elementを消す前に、上記の鍵退避・回復を終える
- [ ] [Element X](https://element.io/en/download)をインストールする
- [ ] 同じMatrixアカウントでログインする
- [ ] リカバリーキーまたは検証済み端末で検証する
- [ ] Secure Backupへ接続できていることを確認する
- [ ] 複数の過去メッセージを復号できることを確認する
- [ ] 確認後、旧Elementを削除する

## 4. 最終確認

- [ ] 使用中の端末がすべてVerifiedになっている
- [ ] Secure Backupが有効である
- [ ] リカバリーキーを安全に保管している
- [ ] Element Xで過去の暗号化メッセージを読める
- [ ] 不要な古いセッションは、上記確認後にだけ削除した

## 公式資料

- [How to Verify Devices](https://docs.element.io/latest/element-support/device-verification/how-to-verify-devices/)
- [How to Ensure You Have a Recovery Key](https://docs.element.io/latest/element-support/device-verification/how-to-ensure-you-have-a-recovery-key/)
- [Resetting the server-side key backup](https://element.io/blog/resetting-the-server-side-key-backup/)
- [Export and Import E2E Room Keys](https://docs.element.io/ess-classic-lts-24.10/element-support/cross-signing/export-and-import-e2e-room-keys/)

