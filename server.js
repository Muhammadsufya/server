const express = require('express');
const ytdl = require('ytdl-core');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static('public'));

app.get('/download', async (req, res) => {
    const videoURL = req.query.url;
    const format = req.query.format || 'mp4';
    const quality = req.query.quality || 'highest';

    if (!ytdl.validateURL(videoURL)) {
        return res.status(400).send('Invalid YouTube URL');
    }

    try {
        const info = await ytdl.getInfo(videoURL);
        const title = info.videoDetails.title.replace(/[^a-zA-Z0-9]/g, '_');
        const extension = format === 'audio' ? 'mp3' : 'mp4';

        res.header('Content-Disposition', `attachment; filename="${title}.${extension}"`);

        ytdl(videoURL, {
            format: format === 'audio' ? 'audioonly' : 'video',
            quality: quality,
        }).pipe(res);
    } catch (err) {
        res.status(500).send('Failed to download video');
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
