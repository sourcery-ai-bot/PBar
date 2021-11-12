#! /bin/env python3.9

"""
HTML generator for the different languages of the page. This will hopefully help when doing
some changes to the markup, so we don't need to edit the same thing on all the html files.

This script will grab the langs.json file with all the labels to use.
"""



HTML_CONTENT = """\
<!DOCTYPE html>
<!--
	This page was initialy made as homework for school.
	One of the handicaps was not being able to use JavaScript, or any other scripting language.
	That's why this page lacks a bit of it.
-->

<html lang="{lang}">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title> PBar - {bannerSubtitle} </title>
	<link rel="stylesheet" href="styles/main.css">
</head>
<body>
	<div class="lang-changer">
		{langChanger}
	</div>

	<div class="banner">
		<h1 class="banner-title">PBar</h1>
		<span class="banner-subtitle">{bannerSubtitle}</span>
	</div>

	<div class="info">
		<div class="info-item blue">
			<h1>{infoItem1_heading}</h1>
			<p>
				{infoItem1_text}
			</p>
			<a class="button" href="#showcase1">{infoItem1_button}</a>
		</div>
		<div class="info-item red">
			<h1>{infoItem2_heading}</h1>
			<p>
				{infoItem2_text}
			</p>
			<a class="button" href="#showcase1">{infoItem2_button}</a>
		</div>
		<div class="info-item purple">
			<h1>{infoItem3_heading}</h1>
			<p>
				{infoItem3_text}
			</p>
			<a target="_blank" class="button" href="https://github.com/DarviL82/PBar/wiki">{infoItem3_button}</a>
		</div>
	</div>







	<div class="showcase part1" id="showcase1">
		<h1 class="show-title">{showcase1_title}</h1>
		<div class="show code left">
			<code>
				<span class="kw">import</span> <span class="obj">pbar</span>

				<span class="var">myBar</span> <span class="op">=</span> <span class="obj">pbar</span>.<span class="obj">PBar</span>()
				<span class="var">myBar</span>.<span class="func">draw</span>()
			</code>
		</div>
		<div class="show content right">
			<p>{showcase1_text}</p>
		</div>
	</div>


	<div class="showcase part2">
		<h1 class="show-title">{showcase2_title}</h1>
		<div class="show content left">
			<p>{showcase2_text}</p>
		</div>
		<div class="show code right">
			<code>
				<span class="func">@</span><span class="obj">pbar</span>.<span class="func">taskWrapper</span>(<span class="var">myBar</span>, <span class="func">locals</span>())
				<span class="kw">def</span><span class="func"> my_task</span>():
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="func">get_data</span>()
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="func">process_stuff</span>()
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="func">show_data</span>()
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="func">useless_function</span>()
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="func">another_function</span>()
			</code>
		</div>
	</div>


	<div class="showcase part3">
		<h1 class="show-title">{showcase3_title}</h1>
		<div class="show code left">
			<code>
				<span class="kw">def</span><span class="func"> my_task</span>():
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="func">get_data</span>()
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="var">myBar</span>.<span class="func">step</span>()
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="func">process_stuff</span>()
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="var">myBar</span>.<span class="func">step</span>()
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="func">show_data</span>()
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="var">myBar</span>.<span class="func">step</span>()
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="func">useless_function</span>()
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="var">myBar</span>.<span class="func">step</span>()
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="func">another_function</span>()
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="var">myBar</span>.<span class="func">step</span>()
			</code>
		</div>
		<div class="show content right">
			<p>{showcase3_text}</p>
		</div>
	</div>


	<div class="showcase part4" id="showcase4">
		<h1 class="show-title">{showcase4_title}</h1>
		<div class="show content" style="width: 100%;">
			<p>{showcase4_text}</p>
		</div>
		<code>	<!-- turture -->
			<span class="var">conds</span> <span class="op">=</span> (
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="obj">pbar</span>.<span class="obj">Cond</span>(<span class="str">"percentage >= 50"</span>, </span><span class="obj">pbar</span>.<span class="obj">ColorSet</span>.YELLOW, <span class="obj">pbar</span>.<span class="obj">CharSet</span>.BRICKS),
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="obj">pbar</span>.<span class="obj">Cond</span>(<span class="str">"percentage == 100"</span>, </span><span class="obj">pbar</span>.<span class="obj">ColorSet</span>.GREEN),
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="obj">pbar</span>.<span class="obj">Cond</span>(<span class="str">"text <- error"</span>, <span class="obj">pbar</span>.<span class="obj">ColorSet</span>.RED, <span class="var">formatset</span><span class="op">=</span><span class="obj">pbar</span>.<span class="obj">FormatSet</span>.DESCRIPTIVE)
			)

			<span class="var">myBar</span> <span class="op">=</span> <span class="obj">pbar</span>.<span class="obj">PBar</span>(<span class="var">conditions</span><span class="op">=</span><span class="var">conds</span>)

			<span class="kw">try</span>:
			&nbsp;&nbsp;&nbsp;&nbsp;<span class="obj">pbar</span>.<span class="func">animate</span>(<span class="var">myBar</span>, <span class="obj">range</span>(<span class="num">50</span>))
			<span class="kw">except</span>:
			&nbsp;&nbsp;&nbsp;&nbsp;<span class="var">myBar</span>.<span class="var">text</span> <span class="op">=</span> <span class="str">"Error!"</span>
			&nbsp;&nbsp;&nbsp;&nbsp;<span class="var">myBar</span>.<span class="func">draw</span>()

		</code>

		<video width="100%" autoplay loop muted>
			<source src="https://raw.githubusercontent.com/DarviL82/PBar/main/resources/examples/conds.mp4" type="video/mp4">
		</video>

	</div>




	<div class="links">
		<h1 style="font-size: 2.5em">{links_title}</h1>
		<div class="items">
			<a class="link" target="_blank" href="https://pypi.org/project/PBar2/">
				<img src="images/pypi.svg" alt="">
				<h2 class="link-title">Python Package Index</h2>
				<p class="link-text">
					{link1_text}
				</p>
			</a>
			<a class="link" target="_blank" href="https://github.com/DarviL82/PBar">
				<img src="images/github.png" alt="">
				<h2 class="link-title">GitHub</h2>
				<p class="link-text">
					{link2_text}
				</p>
			</a>
			<a class="link" target="_blank" href="https://aur.archlinux.org/packages/python-pbar/">
				<img src="images/arch.png" alt="">
				<h2 class="link-title">Arch User Repository</h2>
				<p class="link-text">
					{link3_text}
				</p>
			</a>
		</div>
	</div>



	<footer>
		<div class="credits-logo" style="margin-right: 20px">
			<img src="images/logo.png">
		</div>
		<div class="credits-content">
			<h3>David Losantos</h3>
			<a target="_blank" href="https://github.com/DarviL82/"><img class="credits-img" style="filter: invert()" src="images/github.png"></a>
			<a target="_blank" href="https://twitter.com/DarviL82_"><img class="credits-img" src="images/twitter.png"></a>
		</div>
	</footer>
</body>
<script src="scripts/main.js"></script>

</html>
"""



# {
# 	"bannerSubtitle": "",

# 	"infoItem1_heading": "",
# 	"infoItem1_text": "",
# 	"infoItem1_button": "",

# 	"infoItem2_heading": "",
# 	"infoItem2_text": "",
# 	"infoItem2_button": "",

# 	"infoItem3_heading": "",
# 	"infoItem3_text": "",
# 	"infoItem3_button": "",

# 	"showcase1_title": "",
# 	"showcase1_text": "",

# 	"showcase2_title": "",
# 	"showcase2_text": "",

# 	"showcase3_title": "",
# 	"showcase3_text": "",

# 	"showcase4_title": "",
# 	"showcase4_text": "",

# 	"links_title": "",
# 	"link1_text": "",
# 	"link2_text": "",
# 	"link3_text": "",
# },



import json


def main():
	with open("langs.json", "r") as langsFile:	# load json file with languages
		LANGUAGES = json.load(langsFile)


	for lang, labels in LANGUAGES.items():
		langChanger = "".join(	# add the language selector, which only shows the other languages, not the current one.
			f"<a href={'index' if lc == 'en' else lc}.html> {labels['langName']} </a>"
			for lc, labels in LANGUAGES.items() if lc != lang)

		labels = LANGUAGES["en"] | labels	# merge with english dict, in case some labels are missing.

		with open(f"{'index' if lang == 'en' else lang}.html", "w") as file:
			labels["lang"] = lang	# we now set both the lang and langchanger values for the HTML
			labels["langChanger"] = langChanger
			file.write(HTML_CONTENT.format(**labels))


main()