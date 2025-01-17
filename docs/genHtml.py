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
	<link rel="icon" href="images/favicon.png">

	<link rel="stylesheet" href="styles/main.css">
</head>
<body class="preload">
	<div class="lang-changer">
		<svg onclick="showLanguagePrompt()" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-translate" viewBox="0 0 16 16">
			<path d="M4.545 6.714 4.11 8H3l1.862-5h1.284L8 8H6.833l-.435-1.286H4.545zm1.634-.736L5.5 3.956h-.049l-.679 2.022H6.18z"/>
			<path d="M0 2a2 2 0 0 1 2-2h7a2 2 0 0 1 2 2v3h3a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-3H2a2 2 0 0 1-2-2V2zm2-1a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h7a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H2zm7.138 9.995c.193.301.402.583.63.846-.748.575-1.673 1.001-2.768 1.292.178.217.451.635.555.867 1.125-.359 2.08-.844 2.886-1.494.777.665 1.739 1.165 2.93 1.472.133-.254.414-.673.629-.89-1.125-.253-2.057-.694-2.82-1.284.681-.747 1.222-1.651 1.621-2.757H14V8h-3v1.047h.765c-.318.844-.74 1.546-1.272 2.13a6.066 6.066 0 0 1-.415-.492 1.988 1.988 0 0 1-.94.31z"/>
		</svg>

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
			<a class="button" href="#showcase4">{infoItem2_button}</a>
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
	<span class="func">get_data</span>()
	<span class="func">process_stuff</span>()
	<span class="func">show_data</span>()
	<span class="func">useless_function</span>()
	<span class="func">another_function</span>()
			</code>
		</div>
	</div>


	<div class="showcase part3">
		<h1 class="show-title">{showcase3_title}</h1>
		<div class="show code left">
			<code>
<span class="kw">def</span><span class="func"> my_task</span>():
	<span class="func">get_data</span>()
	<span class="var">myBar</span>.<span class="func">step</span>()
	<span class="func">process_stuff</span>()
	<span class="var">myBar</span>.<span class="func">step</span>()
	<span class="func">show_data</span>()
	<span class="var">myBar</span>.<span class="func">step</span>()
	<span class="func">useless_function</span>()
	<span class="var">myBar</span>.<span class="func">step</span>()
	<span class="func">another_function</span>()
	<span class="var">myBar</span>.<span class="func">step</span>()
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
	<span class="obj">pbar</span>.<span class="obj">Cond</span>(<span class="str">"percentage >= 50"</span>, </span><span class="obj">pbar</span>.<span class="obj">ColorSet</span>.YELLOW, <span class="obj">pbar</span>.<span class="obj">CharSet</span>.BRICKS),
	<span class="obj">pbar</span>.<span class="obj">Cond</span>(<span class="str">"percentage == 100"</span>, </span><span class="obj">pbar</span>.<span class="obj">ColorSet</span>.GREEN),
	<span class="obj">pbar</span>.<span class="obj">Cond</span>(<span class="str">"text <- error"</span>, <span class="obj">pbar</span>.<span class="obj">ColorSet</span>.RED, <span class="var">formatset</span><span class="op">=</span><span class="obj">pbar</span>.<span class="obj">FormatSet</span>.DESCRIPTIVE)
)

<span class="var">myBar</span> <span class="op">=</span> <span class="obj">pbar</span>.<span class="obj">PBar</span>(<span class="var">conditions</span><span class="op">=</span><span class="var">conds</span>)

<span class="kw">try</span>:
	<span class="obj">pbar</span>.<span class="func">animate</span>(<span class="var">myBar</span>, <span class="obj">range</span>(<span class="num">50</span>))
<span class="kw">except</span> <span class="obj">KeyboardInterrupt</span>:
	<span class="var">myBar</span>.<span class="var">text</span> <span class="op">=</span> <span class="str">"Error!"</span>
	<span class="var">myBar</span>.<span class="func">draw</span>()
		</code>

		<video width="100%" autoplay loop muted>
			<source src="https://raw.githubusercontent.com/DarviL82/PBar/main/resources/examples/conds.mp4" type="video/mp4">
		</video>

	</div>


	<div class="showcase part5">
		<h1 class="show-title">{showcase5_title}</h1>
		<div class="show content" style="width: 100%;">
			<p>{showcase5_text1}</p>
		</div>

		<video width="100%" autoplay loop muted controls>
			<source src="https://user-images.githubusercontent.com/48654552/140072905-f83a1ff4-fba7-481d-925d-727caed6c3e8.mp4" type="video/mp4">
		</video>

		<div class="show content" style="width: 100%;">
			<p>
				{showcase5_text2}
			</p>
			<a target="_blank" href="https://github.com/DarviL82/PBar/wiki" class="button">{showcase5_button}</a>
		</div>

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
			<a style="position: relative" target="_blank" href="https://discord.gg/">
				<img class="credits-img" src="images/discord.png"> <span class="mshow"> DarviL#3242 </span>
				<div class="tooltip"> DarviL#3242 </div>
			</a>
		</div>
	</footer>
</body>
	<script src="https://darvil82.github.io/DarviLStuff/web/promptTest/prompt.js"></script>
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

#	"showcase5_title": "",
#	"showcase5_text1": "",
#	"showcase5_text2": "",
#	"showcase5_button": "",

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
		labels = LANGUAGES["en"] | labels	# merge with english dict, in case some labels are missing.

		with open(f"{'index' if lang == 'en' else lang}.html", "w") as file:
			labels["lang"] = lang	# we now set the lang values for the HTML
			file.write(HTML_CONTENT.format(**labels))


main()
