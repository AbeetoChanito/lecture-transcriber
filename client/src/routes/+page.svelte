<script lang="ts">
    let files: FileList | null = null;
    let uploadError: any = null;
    let videoTranscribed: string | null = null;

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

    $: if (files) {
        (async () => {
            console.log("File updated");

            let file: File = files[0];

            let formData = new FormData();
            formData.append("file", file);

            try {
                const response = await uploadFile(formData);
                videoTranscribed = response["video_transcribed"];
                console.log(`Video transcribed: ${videoTranscribed}`);
            } catch (error) {
                uploadError = error;
                console.log(`Error uploading file: ${uploadError}`);
            }

            files = null;
        })();
    }
</script>

<label for="video">Upload a video:</label>
<input accept="video/mp4" bind:files id="video" name="video" type="file"/>

{#if uploadError}
    <p>Error uploading file! {uploadError}</p>
{/if}

{#if videoTranscribed}
    <p>Video transcribed: {videoTranscribed}</p>
{/if}