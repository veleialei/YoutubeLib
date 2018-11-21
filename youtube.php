<?php

$keyword = $_GET["keyword"];
$url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=".urlencode($keyword)."&key=AIzaSyBRG1jU1v7YlpfCNcC2uOyyyx8l3EjyJ60";
$content = file_get_contents($url);

$data = json_decode($content);
$page_token = $data->nextPageToken;

$base_url = "https://www.youtube.com/watch?v=";

$list = [];
foreach ($data->items as $key => $v) {
  if(property_exists($v->id, "videoId")){
    $videoId = $v->id->videoId;
    $url = $base_url.$videoId;
    $title = $v->snippet->title;
    $icon = $v->snippet->thumbnails->high->url;


    $path = "{$videoId}.mp3";
    $list[] = ["id"=>$videoId, "path"=>$path, "url"=>$url, "title"=>$title, "icon"=>$icon];

  }


}
echo json_encode(["page_token"=>$page_token, "list"=>$list])