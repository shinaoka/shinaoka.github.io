---
layout: single
title: "Matrix Encryption Setup Checklist for New Users"
date: 2026-08-17
lang: en
excerpt: "A first-day checklist for configuring a recovery key, Secure Backup, and verified devices before relying on encrypted Matrix chats."
permalink: /blog/matrix-encryption-setup-checklist/
toc: true
toc_label: "Contents"
---

**Language:** [日本語](/blog/matrix-encryption-setup-checklist-ja/) / English

**For:** **New Matrix users** / [Existing users](/blog/matrix-encryption-safety-recovery-checklist/)

<div class="notice--danger" markdown="1">
## Complete this before relying on Matrix chat

The keys needed to read encrypted Matrix messages are managed separately from your account password. If you postpone Secure Backup and recovery-key setup, a lost device or a missed room key may leave some messages permanently unreadable.
</div>

## What you need to know

- A **recovery key is not your login password**. Your service administrator cannot retrieve it for you later.
- **Secure Backup** is Matrix's standard recovery mechanism. It encrypts room keys received by your device and stores the encrypted backup on the server.
- **Device verification** cryptographically confirms that a new login session belongs to you.
- On phones, use **Element X**, not the legacy Element/Element Classic app.

## Recommended client by operating system

| OS | Recommended client | Encryption-recovery role |
| --- | --- | --- |
| Windows | **Element Desktop** | Element X is not available for Windows, so keep this as a verified reference session connected to Secure Backup |
| macOS | **Element Desktop**; Element X can be added on supported Macs | Element X can provide an additional verified session |
| iPhone / Android | **Element X** | Verify it after login and connect it to Secure Backup |

Windows users can use encrypted Matrix rooms safely without Element X. Verify Element Desktop, store the recovery key, and confirm that Secure Backup is active.

## First-day checklist

### 1. Set up the first device and recovery key

- [ ] Sign in to Element for the first time
- [ ] Complete the Secure Backup setup flow
- [ ] If no setup flow appears, open **Settings → Encryption → Get recovery key**
- [ ] Save the generated recovery key somewhere safe

Good storage choices include a password manager, encrypted removable storage, or a printed copy kept in a locked location. Do not store it in a chat message, ordinary email, or an unencrypted note.

In Element Desktop, **Get recovery key** means that one has not been configured. **Change recovery key** means that recovery is configured.

### 2. Verify the first device

- [ ] In Element Desktop, open **profile picture → All Settings → Sessions**
- [ ] Confirm that **Current Session** has a green shield
- [ ] Confirm on the Encryption page that Secure Backup is active

### 3. Add Element X on your phone

- [ ] Install [Element X](https://element.io/en/download) on your phone
- [ ] Sign in with the same Matrix account
- [ ] Verify the session using your recovery key or an existing verified device
- [ ] Confirm that Element X can decrypt older encrypted messages

On supported Macs (Apple Silicon and macOS 15.5 or later), [Element X for Mac](https://apps.apple.com/app/element-x-secure-chat-call/id1631335820) can provide an additional recovery-capable client.

<div class="notice--warning" markdown="1">
**Installing Element X is not enough.** Sign in, complete verification, and confirm that older messages decrypt correctly.
</div>

## Completion criteria

You are ready when all of the following are true:

- [ ] At least one signed-in device is verified
- [ ] Secure Backup is active
- [ ] A valid recovery key is stored safely
- [ ] Element X is signed in and verified
- [ ] Older encrypted messages are readable on at least two devices

## Already using Matrix?

If you have not confirmed your recovery key, verified devices, and Secure Backup, do not log out or reinstall yet. Follow the [safety and recovery checklist for existing users](/blog/matrix-encryption-safety-recovery-checklist/) first.

## Official references

- [How to Ensure You Have a Recovery Key](https://docs.element.io/latest/element-support/device-verification/how-to-ensure-you-have-a-recovery-key/)
- [How to Verify Devices](https://docs.element.io/latest/element-support/device-verification/how-to-verify-devices/)
- [Element Sessions](https://docs.element.io/latest/element-support/element-webdesktop-client-settings/sessions/)
- [Element downloads](https://element.io/en/download)
