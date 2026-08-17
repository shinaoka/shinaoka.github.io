---
layout: single
title: "Matrix Encryption Safety and Recovery Checklist for Existing Users"
date: 2026-08-17
lang: en
excerpt: "A decision-based procedure for preserving existing room keys while fixing device verification, Secure Backup, and recovery-key configuration."
permalink: /blog/matrix-encryption-safety-recovery-checklist/
toc: true
toc_label: "Contents"
---

**Language:** [日本語](/blog/matrix-encryption-safety-recovery-checklist-ja/) / English

**For:** [New Matrix users](/blog/matrix-encryption-setup-checklist/) / **Existing users**

<div class="notice--danger" markdown="1">
## Do not lose your currently signed-in devices while checking recovery

Do not sign out, reinstall an app, delete a session, or reset Secure Backup or your cryptographic identity yet. A device that can currently read old messages may hold the only remaining copy of room keys that were never backed up.
</div>

## Completion criteria

- [ ] At least one signed-in device is verified
- [ ] Secure Backup is active
- [ ] A valid recovery key is stored safely
- [ ] Element X is signed in and verified on your phone
- [ ] Older encrypted messages are readable on at least two devices

## 1. Inventory your current sessions

- [ ] In Element Desktop, open **profile picture → All Settings → Sessions**
- [ ] Look for the green shield on **Current Session**
- [ ] Review **Other Sessions → Verified: Ready for secure messaging**
- [ ] Record active devices under **Unverified: Not ready for secure messaging**

The device list on `account.matrix.org` manages login sessions; it does not reliably show cryptographic verification. Use the green shield and Verified filter in Element. Element Desktop and Koushi on the same computer are separate Matrix devices.

### Choose the matching path

1. **You have a verified device** → [2A](#2a-you-have-a-verified-device)
2. **No verified device, but an Element Desktop session can read old messages** → [2B](#2b-no-verified-device-but-old-messages-are-readable)
3. **No recovery key, verified device, or readable signed-in session remains** → [2C](#2c-no-recovery-path-remains)

## 2A. You have a verified device

- [ ] Choose a verified device that can read old messages as the reference device; keep it signed in
- [ ] Open **Settings → Encryption** on that device
- [ ] If you see **Get recovery key**, configure Secure Backup and a recovery key
- [ ] If you see **Change recovery key** but no longer have the current key, change it
- [ ] Store the new recovery key safely
- [ ] Confirm that Secure Backup is active and uploading keys
- [ ] Enter the recovery key on other devices and verify them
- [ ] Confirm that old encrypted messages are readable on every device

## 2B. No verified device, but old messages are readable

Before resetting anything, preserve the keys held by every readable Element Desktop session.

- [ ] Keep all readable Element Desktop sessions open
- [ ] On each one, run **Security & Privacy → Export E2E room keys**
- [ ] Protect each export with a strong passphrase and store it safely
- [ ] If several sessions are readable, export separately from each one
- [ ] Confirm that every export file was actually written

<div class="notice--warning" markdown="1">
**Do not reset Secure Backup from Element X if you can avoid it.** Element X cannot export the complete set of room keys, so keys that are not local to that device may be lost.
</div>

Only after the exports are safe, use Element Desktop to continue:

- [ ] Reset the cryptographic identity and Secure Backup
- [ ] Generate and safely store a new recovery key
- [ ] Verify the reference device
- [ ] Import every E2E room-key export into the reference device
- [ ] Enable Secure Backup and wait for imported keys to be backed up
- [ ] Verify other devices and enter the new recovery key
- [ ] Confirm old-message decryption on each device

## 2C. No recovery path remains

If you have no valid recovery key, verified device, or signed-in session that can read the old messages, the previous room keys cannot be recovered. A service administrator cannot decrypt them for you.

- [ ] Accept that old encrypted history may be lost
- [ ] Reset the cryptographic identity in Element Desktop
- [ ] Generate and store a new recovery key
- [ ] Enable Secure Backup
- [ ] Verify every device you intend to use

## 3. Move phones to Element X

This section applies to phones and supported Macs. **Element X is not available for Windows.** On Windows, keep Element Desktop as a verified reference session and protect recovery with your recovery key and Secure Backup.

- [ ] Before removing legacy Element, finish the key exports and recovery work above
- [ ] Install [Element X](https://element.io/en/download)
- [ ] Sign in with the same Matrix account
- [ ] Verify it with the recovery key or an existing verified device
- [ ] Confirm that it connects to Secure Backup
- [ ] Check several older encrypted messages
- [ ] Only then remove legacy Element from the phone

## 4. Final check

- [ ] All active devices are Verified in Element's Sessions page
- [ ] Secure Backup is active
- [ ] The recovery key is stored safely
- [ ] Element X can read old encrypted messages
- [ ] Old unused sessions were removed only after all checks passed

## Official references

- [How to Verify Devices](https://docs.element.io/latest/element-support/device-verification/how-to-verify-devices/)
- [How to Ensure You Have a Recovery Key](https://docs.element.io/latest/element-support/device-verification/how-to-ensure-you-have-a-recovery-key/)
- [Resetting the server-side key backup](https://element.io/blog/resetting-the-server-side-key-backup/)
- [Export and Import E2E Room Keys](https://docs.element.io/ess-classic-lts-24.10/element-support/cross-signing/export-and-import-e2e-room-keys/)
