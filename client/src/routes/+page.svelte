<script lang="ts">
let files: FileList | null = null;
let videoUrl: string | null = null;
let uploadError: any = null;
let videoTranscribed: string | null = null;
let submitted: boolean = false;
let output: string | null = null;

async function uploadFile(formData: FormData): Promise<any> {
    console.log("Fetching");

    let response = await fetch("/upload_video", {
        method: "POST",
        body: formData
    });

    console.log("Fetched");

    if (!response.ok) {
        let data = await response.json();
        throw new Error(data["error"]);
    }

    return await response.json();
}

async function submit(): Promise<void> {
    submitted = true;

    output = "Processing...";

    let file = files?.[0] as File;

    let formData = new FormData();
    formData.append("file", file);

    try {
        const response = await uploadFile(formData);
        videoTranscribed = response["video_transcribed"];
        output = `Video transcribed:\n${videoTranscribed}`;
    } catch (error) {
        uploadError = error;
        output = `Error uploading file:\n${uploadError}`;
    }

    console.log(output);

    files = null;
}

$: if (files) {
    (async () => {
        console.log("File updated");

        let file = files[0];
        
        videoUrl = URL.createObjectURL(file);
    })();
}
</script>

<svelte:head>
    <title>Video Transcriber</title>
    <link href="https://fonts.googleapis.com/css?family=Lexend" rel="stylesheet">
</svelte:head>

<style>
    body {
        font-family: lexend;
        margin: 0;
    }

    .nav {
        overflow: hidden;
        background-color: #b108ffee;
        display: flex;
        align-items: center;
        padding: 10px 0;
    }

    .nav a {
        color: #f2f2f2;
        padding: 14px 16px;
        text-decoration: none;
        font-size: 50px;
        left: 10px;
    }

    .nav .credit {
        color: #f2f2f2;
        font-size: 20px;
        padding: 25px;
        text-decoration: underline;
    }

    .upload-video {
        width: 500px;
        height: auto;
        padding: 25px;
        margin: 10px 0;
        border: 2px solid #ccc;
        box-sizing: border-box;
        position: relative;
        left: 10px;
    }

    .upload-video label {
        font-size: 20px;
    }

    .upload-video input {
        font-size: 20px;
    }

    .upload-video button {
        font-size: 20px;
    }

    .video-container video {
        margin-left: 10px;
        width: 50%;
        height: 50%;
    }

    .output {
        width: 1000px;
        height: auto;
        padding: 25px;
        margin: 10px 0;
        border: 2px solid #ccc;
        box-sizing: border-box;
        position: relative;
        left: 10px;
        font-size: 10px;
        white-space: pre-line;
    }
</style>

<body>

<div class="nav">
    <a href="/">Video Transcriber</a>
    <a href="https://github.com/AbeetoChanito" class="credit" target="_blank">made by Abinav Kumar</a>
</div>

<div class="upload-video">
<label for="video">Upload a video:</label>
<input accept="video/mp4" bind:files id="video" name="video" type="file"/>
<br>
{#if files}
<button on:click={submit} style={submitted ? 'display: none' : ''}>Submit Video</button>
{/if}
</div>

<div class="video-container">
{#if videoUrl}
<video controls>
    <source src={videoUrl} />
    <track kind="captions" />
</video>
{/if}
</div>

{#if output} 
    <div class="output">
    <h1>{output}</h1>
    </div>
{/if}
</body>