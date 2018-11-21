Side Project: Youtube MP3 Library
==================================================

### Overview

This is the backend and basic webfront end of Youtube MP3 library.

Submit a youtube url. It can store the video or audio format data into mp3 and upload to the firebase storage and database.

It use python Flask as frame work and youtube-dl plugin to convert the files.

### API

<details>
<summary>GET / or /index</summary>

Responses:

<table>
	<tr><td>Code</td><td>Description</td></tr>
	<tr><td>200</td><td>Welcome Page<br/>
<pre>
[
	{
		"eventid": 0,
		"eventname": "string",
		"userid": 0,		
		"avail": 0,
		"purchased": 0
	}
]
	</pre></td></tr>

</table>
</details>


<details>
<summary>GET /upload </summary>

Responses:

<table>
	<tr><td>Code</td><td>Description</td></tr>
	<tr><td>200</td><td>Upload Form
<pre>
{
	"eventid": 0
}
</pre></td></tr>
</details>

<details>
<summary>POST /upload </summary>

Body:

<pre>
{
	"userid": 0,
	"eventname": "string",
	"numtickets": 0
}
</pre>

Responses:

<table>
	<tr><td>Code</td><td>Description</td></tr>
	<tr><td>200</td><td>MP3 is converting
<pre>
{
	"eventid": 0
}
</pre></td></tr>
	<tr><td>400</td><td>Url is invalid</td></tr>
</table>
</details>





<details>
<summary>GET /wishlist </summary>

Responses:

<table>
	<tr><td>Code</td><td>Description</td></tr>
	<tr><td>200</td><td>WishList
<pre>
{
	"eventid": 0
}
</pre></td></tr>
</details>

<details>
<summary>POST /wishlist </summary>

Body:

<pre>
{
	"userid": 0,
	"eventname": "string",
	"numtickets": 0
}
</pre>

Responses:

<table>
	<tr><td>Code</td><td>Description</td></tr>
	<tr><td>200</td><td>Edit successfully
<pre>
{
	"eventid": 0
}
</pre></td></tr>
</table>
</details>




<details>
<summary>GET /musics</summary>

Responses:

<table>
	<tr><td>Code</td><td>Description</td></tr>
	<tr><td>200</td><td>Music List<br/>
<pre>
{
	"eventid": 0,
	"eventname": "string",
	"userid": 0,		
	"avail": 0,
	"purchased": 0
}
</pre></td></tr>
</table>
</details>