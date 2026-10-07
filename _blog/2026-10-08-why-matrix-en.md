---
layout: single
title: "Why Matrix? Escaping Vendor Lock-in in Research Chat"
date: 2026-10-08 06:00:00 +0900
lang: en
excerpt: "Slack, Zulip, Discord: research chat is split across projects, and each platform locks you into its vendor. This post explains, for newcomers, why the open Matrix protocol is an answer, why it has been slow to spread in Asia, and what changed once AI coding agents arrived."
permalink: /blog/why-matrix/
toc: true
toc_label: "Contents"
---

**Language:** [日本語](/blog/naze-matrix-ja/) / English

**For:** people who have heard of Matrix but are not sure why it is worth the switch. For the setup steps, see the [setup checklist for new users](/blog/matrix-encryption-setup-checklist/).

## Research chat is fragmented

Every new collaboration seems to come with a new chat tool. The lab is on Slack, one international project uses Zulip, a software community lives on Discord, and another collaboration has its own Slack workspace. Before sending someone a direct message, you first have to remember where you talk to that person. Notifications are scattered across apps.

What bothers me more than the inconvenience is that **each of these is a single vendor's service**.

- Pricing and free-plan terms change at the vendor's discretion. Many of us remember when old messages disappeared from Slack's free plan.
- The conversation history lives on the vendor's servers, and moving it elsewhere is hard.
- If the service changes direction or shuts down, all users can do is look for somewhere else to go.
- If you need a feature or a bug fix, you file a request and wait.

Research discussions are records we want to keep for years. Leaving them entirely to one company's decisions is the problem I want to solve.

## What Matrix is

[Matrix](https://matrix.org/) is an open, decentralized chat protocol. The idea is close to email.

- There are many servers (homeservers) around the world, and you create an account on one of them.
- You can talk with people on other servers in the same rooms, without thinking about where they are hosted.
- Your ID looks like `@username:server`, and one ID is enough, like an email address.
- The protocol is open, so anyone can build clients (apps) and servers.

Even if your lab, your collaborators, and an international project each run their own server, you can join all of them with one account and one app. You can run your own server or use a public one such as [matrix.org](https://matrix.org/). Users always keep the option to move to another server or switch clients. That is Matrix's answer to vendor lock-in.

Direct messages and private rooms are end-to-end encrypted by default: messages are encrypted on your device, so the server stores only ciphertext and even the server administrator cannot read them.

## Research institutions already rely on it

Matrix is not a hobbyist technology. Research institutions and universities, mainly in Europe, have adopted it as their official chat platform.

<!-- TODO: add links to each institution's official page -->
- Max Planck Society
- Fritz Haber Institute
- Helmholtz Association
- German Aerospace Center (DLR)
- Forschungszentrum Jülich
- GFZ Helmholtz Centre for Geosciences
- CISPA Helmholtz Center for Information Security
- TU Wien
- ETH Zürich, Department of Physics
- Karlsruhe Institute of Technology (KIT)
- TU Dresden
- Technical University of Munich (TUM)
- TU Berlin
- LMU Munich
- TU Darmstadt
- University of Augsburg, Institute of Physics
- University of Strasbourg
- New York University (HSRN VIP)
- University of Twente (Studenten Net Twente)

Each runs its own homeserver and still talks with outside researchers across servers.

## Why it has been slow to spread in Asia

Adoption in Asia has lagged behind Europe and North America. I see two main reasons.

**The first is support for non-Latin scripts.** The Matrix ecosystem has been driven mostly by developers in Europe and North America, and Chinese, Japanese, and Korean (CJK) text tended to be an afterthought. In Element Desktop, the official client, searching for a Japanese word often failed to find messages that clearly contained it. For a tool you use every day, that is a dealbreaker.

**The second is that the security settings are hard to understand.** Matrix is very flexible, including in how encryption is managed. As a result, newcomers do not know what they need to set up. They skip the recovery key or device verification described below, and later find that a new device cannot read their past messages.

Both are client problems, not protocol problems. And that is what is now changing.

## AI coding agents made building clients feasible

Because the protocol is open, anyone unhappy with existing clients can build their own. Until recently, though, building a chat client with end-to-end encryption was a job for a dedicated team.

AI coding agents such as Claude Code and Codex changed that. Official SDKs such as [matrix-rust-sdk](https://github.com/matrix-org/matrix-rust-sdk) handle the hard parts, encryption and sync, and you build the interface and user experience on top together with an AI agent. Small teams and even individuals can now produce usable clients.

Indeed, a wave of new clients has appeared in 2026.

- **[Koushi](https://github.com/shinaoka/koushi-matrix)**: a desktop client I am building together with AI coding agents. It tackles Japanese input and search head-on, as well as the second problem, confusing security setup. See [the section below](#koushi) for details.
- **[Komai](https://etke.cc/blog/introducing-komai)**: a desktop client from etke.cc, which states openly that it is built by engineers working together with AI coding agents (Claude Code and Codex).
- Others include Mactrix and Relay for macOS, Lightning (Qt), and SchildiChat Revenge (see the [Matrix client list](https://matrix.org/ecosystem/clients/)).

This is the decisive difference from a locked-in service. If Japanese search does not work in Slack, all we can do is file a request. With Matrix, we can build a client that fixes it and start using it with the same account.

## Where newcomers get stuck

Newcomers tend to stumble in the same places. This section explains only why things work the way they do. For the actual steps, see the [setup checklist for new users](/blog/matrix-encryption-setup-checklist/).

### Logging in: which server is your account on?

A Matrix ID has the form `@username:server`. When a login screen asks for your homeserver, enter the part after the colon (`matrix.org` if you signed up there). To create an account, the most reliable route is [Element Web](https://app.element.io/) in a browser.

### Your password and your recovery key are different things

This is the biggest pitfall.

- Your **password** lets you log in.
- Your **recovery key** unlocks the backup of the keys that decrypt your messages.

Messages are encrypted on your devices, so your devices hold the decryption keys. Matrix can back these keys up to the server, encrypted, and the recovery key is what opens that backup. The recovery key is never stored on the server, so **the server administrator cannot recover it for you**. That is exactly why the administrator cannot read your messages either.

**Create and save a recovery key right after you create your account.** Keep it in a password manager, or on paper in a locked place.

### Always verify your own devices; you rarely need to verify other people

Matrix uses the word "verify" for two different things, and many people confuse them. The name is the same, but the purpose and importance are completely different.

![Verifying your own devices: approve the new iPhone from your verified Mac or enter the recovery key, and the iPhone can then receive keys from the encrypted key backup on the server](/assets/images/matrix/verify-own-devices-en.svg)

![Verifying other people: you and a collaborator compare the emoji shown on each screen. Only needed when you must rule out impersonation; chat and encryption work without it](/assets/images/matrix/verify-other-people-en.svg)

| | Verifying your own devices | Verifying other people |
| --- | --- | --- |
| What it does | Confirms that a new device really belongs to you | Confirms that the person you are talking to is genuine |
| Scope | Inside your own account | Between your account and theirs |
| Should you do it? | **Always** | **Only when security is a serious concern** |
| How | Enter your recovery key, or approve from another device of yours | Compare the emoji on both screens, in person or on a call |

#### Verifying your own devices: always do it

Skipping verification of your own devices causes real, practical problems.

- **Keys are not shared, so messages cannot be decrypted.** When you log in on a new device with your password, you see your room list, but every past message shows "Unable to decrypt." Nothing is broken; that device simply has not received the keys. Once it is verified, it can fetch keys from the key backup and read your messages.
- **Other people see warnings.** When others in your rooms send messages, they are warned that you have an unverified device. Depending on their settings, that device will not receive keys for new messages either.

Verification takes seconds: enter your recovery key, or approve from another device of yours that is already verified. **Whenever you log in on a new device, verify it right away.**

<div class="notice--danger" markdown="1">
**If you forget or lose your recovery key, start the recovery procedure immediately.**

Before logging out of any device or deleting the app, work through the [safety and recovery checklist for existing users](/blog/matrix-encryption-safety-recovery-checklist/) from the top. A logged-in device may be the last place holding keys that have not been backed up. If you act while that device is still available, you can move to a new recovery key without losing any keys.
</div>

#### Verifying other people: only when security is a serious concern

Verifying another person is how you confirm that the person you are talking to is genuine, and not someone impersonating them. You connect in person or on a call and check that both screens show the same emoji.

It has nothing to do with handing over keys, so chat and encryption work normally without it. In everyday lab and collaboration chat, you would rarely do it. It is meant for situations where security matters a great deal, such as handling highly confidential information. You do not need to verify everyone.

## Koushi

![The Koushi window: three account tabs across the top, above a three-pane layout with Spaces, the room list, and messages](/assets/images/matrix/koushi-main.png)

[Koushi](https://github.com/shinaoka/koushi-matrix) is a desktop Matrix client that I am building together with AI coding agents. The name is a Japanese pun: *kōshi* means both "photon" (光子), which carries the signal, and "lattice" (格子), a nod to Matrix. It is open source under MIT / Apache-2.0.

I turned my frustrations with existing clients into design goals.

- **Works properly in Japanese, Chinese, and Korean.** Confirming an IME conversion is kept separate from sending, so pressing Enter to confirm a conversion does not send a half-written message. Search works over encrypted history even for text without spaces between words, and treats full-width and half-width characters as the same. The interface is available in English and Japanese.
- **Several accounts in one window.** If you have accounts on, say, your lab's server and on matrix.org, keep them side by side in tabs, all signed in and syncing. This takes the fragmentation problem from the start of this post and shrinks it further within Matrix.
- **What research discussions need.** Markdown, code blocks, LaTeX-style math, and threads.
- **Secure setup you cannot skip.** After you sign in, Koushi does not open the chat view until the device is verified and key backup is set up. Verifying other people, on the other hand, is treated as optional, and Koushi does not warn you merely because you have not done it. This is a direct implementation of the idea in the diagrams above: always verify your own devices; verify other people only when security is a serious concern.

macOS (Apple Silicon) is officially supported. Releases are signed and notarized, and you can download the DMG from [Releases](https://github.com/shinaoka/koushi-matrix/releases/latest). Windows and Linux builds exist but have not been tested yet. If you use Windows or Linux and can test, report bugs, or contribute to development, you are very welcome.

Voice and video calls, screen sharing, bots, and widgets are not supported yet. Since Koushi is still under development, please also keep Element X signed in to the same account. Questions and requests are welcome in the public room [#koushi-matrix:matrix.org](https://matrix.to/#/#koushi-matrix:matrix.org).

## Getting started

1. Install a client (Element X or Koushi on a Mac, Element on Windows, Element X on a phone).
2. Create an account.
3. **Create and save a recovery key right away.**
4. Log in on a second device and verify it with the recovery key.

The [setup checklist for new users](/blog/matrix-encryption-setup-checklist/) walks through these steps.

## Closing thoughts

Chat is the record of our research discussions. I want us to choose where that record lives, rather than leave it to a vendor. Matrix is a practical way to do that, and it is already standard infrastructure at many European research institutions.

Its weak points, such as support for Asian languages and confusing settings, can now be fixed from the user side thanks to AI coding agents. I would like to see Matrix spread among researchers in Asia as well. Please get a Matrix ID and use it as a contact for your collaborations.

## Related posts

- [Matrix Encryption Setup Checklist for New Users](/blog/matrix-encryption-setup-checklist/)
- [Matrix Encryption Safety and Recovery Checklist for Existing Users](/blog/matrix-encryption-safety-recovery-checklist/)
- [Introduction to Matrix for Researchers Tired of Slack](/blog/introduction-to-matrix-for-researchers-tired-of-slack/) (2025)
