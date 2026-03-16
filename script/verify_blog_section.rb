#!/usr/bin/env ruby
# frozen_string_literal: true

def assert(condition, message)
  return if condition

  warn "FAIL: #{message}"
  exit 1
end

site_root = File.expand_path("../_site", __dir__)

def read_file(path)
  File.read(path)
rescue Errno::ENOENT
  nil
end

index_html = read_file(File.join(site_root, "index.html"))
assert(index_html, "missing generated homepage")
assert(index_html.include?("/blog/"), "homepage should link to /blog/")
assert(index_html.include?(">Blog<") || index_html.include?("Blog"), "homepage should expose Blog navigation")

blog_index = File.join(site_root, "blog", "index.html")
blog_html = read_file(blog_index)
assert(blog_html, "missing generated blog index page")
assert(blog_html.include?("/julia_spring_school_2026/"), "blog index should promote julia_spring_school_2026")

teaching_html = read_file(File.join(site_root, "docs", "teaching.html"))
assert(teaching_html, "missing generated teaching page")
assert(teaching_html.include?("/julia_spring_school_2026/"), "teaching page should link to julia_spring_school_2026")

expected_blog_pages = [
  "on-julias-future-developer-experience-in-the-era-of-generative-ai",
  "julia-no-ikirumichi",
  "why-i-migrated-from-cpp-to-rust-development-experience-in-the-age-of-generative-ai",
  "naze-cpp-kara-rust-he-ikoushitaka",
  "cpp-wo-tsukatta-suuchikeisan-library",
  "introduction-to-matrix-for-researchers-tired-of-slack",
  "slack-ni-tsukareta-kenkyusha-no-tame-no-matrix-nyumon"
]

expected_blog_pages.each do |slug|
  assert(
    File.exist?(File.join(site_root, "blog", slug, "index.html")),
    "missing generated blog article page for #{slug}"
  )
end

puts "verify_blog_section: OK"
