## Agentic AI Coding × Rust: 安全に速く研究コードを書く

「物理屋のための機械学習講義」第22回の補助資料ページです。

* 日時: 2026年6月26日(金) 13:00-17:00 JST
* 講師: 品岡 寛 (埼玉大学)
* 講義ページ: [物理屋のための機械学習講義](https://akio-tomiya.github.io/lectures4mlphys/)

## 補助資料

講義の補助資料は，講義の1週間前までを目処にこのページに掲載します．

* スライド: [日本語 (PDF)](https://github.com/shinaoka/agentic-ai-coding-rust/blob/main/slides.pdf) ・ [English (PDF)](https://github.com/shinaoka/agentic-ai-coding-rust/blob/main/slides_en.pdf) （[Typst ソース](https://github.com/shinaoka/agentic-ai-coding-rust)）
* ハンズオン資料: 準備中
* サンプルコード: 準備中

## 概要

近年の大規模言語モデルは，コード補完を超えて，
仕様の整理，実装，テスト，デバッグ，リファクタリングを反復的に行う
“agentic AI coding” の段階に入りつつある．

講師自身もこの半年，手動でコードはほとんど書いておらず，
テンソルネットワークに基づく機械学習的アプローチの物理への応用に向けて，
AI coding agent とともに新しいソフトウェアスタックを開発している．
関連する開発例として，以下がある．

* [tenferro-rs](https://github.com/tensor4all/tenferro-rs): 自動微分と CPU/GPU 対応を備えた汎用テンソル計算ライブラリ
* [tensor4all-rs](https://github.com/tensor4all/tensor4all-rs): Tensor4All のテンソルネットワークエコシステムの Rust 実装

一方で，研究コードでは，数値的正しさ，再現性，性能，
依存関係管理，長期保守性が重要である．

本講義では，物理・機械学習研究における日常的なコード開発を題材に，
AI coding agent を安全に使うためのワークフローを概観する．

特に Rust の型システム，所有権，テスト，パッケージ管理を利用することで，
AI が生成したコードを人間が検証しやすく，
壊れにくい研究ソフトウェアへ効率よく育てる方法を紹介する．

後半では，簡単な数値計算コードを題材に，
AI coding agent と Rust を用いた実装，テストなどを
ハンズオン形式で体験する．
