---
layout: single
title: "Matrixを使い始める前の暗号化設定チェックリスト"
date: 2026-08-17
lang: ja
excerpt: "Matrixを使い始める日に、リカバリーキー、Secure Backup、端末検証を確実に設定するためのチェックリストです。"
permalink: /blog/matrix-encryption-setup-checklist-ja/
toc: true
toc_label: "目次"
---

**言語:** 日本語 / [English](/blog/matrix-encryption-setup-checklist/)

**対象者:** **初めてMatrixを使う人** / [すでに使っている人](/blog/matrix-encryption-safety-recovery-checklist-ja/)

<div class="notice--danger" markdown="1">
## チャットを使い始める前に完了してください

Matrixの暗号化メッセージを読むための鍵は、アカウントのパスワードとは別に管理されます。最初の日にSecure Backupとリカバリーキーを設定しないと、端末の故障や鍵の受信失敗によって、後から読めないメッセージが残ることがあります。
</div>

## まず覚えておくこと

- **リカバリーキーはログインパスワードではありません。** サービス管理者も後から教えることはできません。
- **Secure Backup**は、端末が受信した復号鍵を暗号化してサーバーへ保管するMatrix標準の回復手段です。
- **端末検証**は、新しい端末を自分の正当な端末として暗号学的に承認する操作です。
- スマートフォンでは、従来のElement（Element Classic）ではなく**Element X**を使うことを強く推奨します。

## 利用開始チェックリスト

### 1. 最初の端末とリカバリーキー

- [ ] Elementへ初めてログインした
- [ ] Secure Backupの設定案内を最後まで完了した
- [ ] 案内が表示されない場合、**Settings → Encryption → Get recovery key**を開いた
- [ ] 発行されたリカバリーキーを安全な場所へ保存した

保存先には、パスワードマネージャー、暗号化した外部メディア、施錠できる場所に保管した紙などを使います。チャット内、自分宛てメール、暗号化されていないメモには保存しないでください。

Element Web/DesktopのEncryption画面で、**Get recovery key**と表示される場合は未設定、**Change recovery key**と表示される場合は設定済みです。

### 2. 最初の端末を検証する

- [ ] [Element WebのSessions画面](https://app.element.io/#/settings/sessions)を開いた
- [ ] **Current Session**に緑の盾が表示されている
- [ ] Encryption画面でSecure Backupが有効になっている

直接リンクが開かない場合は、Element Web/Desktopで **プロフィール画像 → All Settings → Sessions** と進みます。

### 3. Element Xを追加する

- [ ] スマートフォンへ[Element X](https://element.io/en/download)をインストールした
- [ ] 同じMatrixアカウントでログインした
- [ ] リカバリーキー、または最初の検証済み端末を使って端末検証を完了した
- [ ] Element Xで過去の暗号化メッセージを読めることを確認した

対応するMac（Apple Silicon、macOS 15.5以降）では、[Mac版Element X](https://apps.apple.com/app/element-x-secure-chat-call/id1631335820)も補助端末として利用できます。

<div class="notice--warning" markdown="1">
**Element Xをインストールしただけでは回復経路になりません。** 同じアカウントでログインし、端末検証と過去メッセージの復号確認まで完了してください。
</div>

## 完了条件

次のすべてを満たせば、利用開始の準備は完了です。

- [ ] 検証済み端末が1台以上ある
- [ ] Secure Backupが有効である
- [ ] 有効なリカバリーキーを安全に保管した
- [ ] Element Xが検証済みである
- [ ] 2台の端末で過去の暗号化メッセージを読める

## すでに使い始めている場合

リカバリーキー、端末検証、Secure Backupのいずれかが未確認なら、ログアウトや再インストールを行う前に[既存利用者向けの安全確認・回復チェックリスト](/blog/matrix-encryption-safety-recovery-checklist-ja/)へ進んでください。

## 公式資料

- [How to Ensure You Have a Recovery Key](https://docs.element.io/latest/element-support/device-verification/how-to-ensure-you-have-a-recovery-key/)
- [How to Verify Devices](https://docs.element.io/latest/element-support/device-verification/how-to-verify-devices/)
- [Element Sessions](https://docs.element.io/latest/element-support/element-webdesktop-client-settings/sessions/)
- [Element downloads](https://element.io/en/download)

