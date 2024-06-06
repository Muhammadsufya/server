from flask import Flask, request, jsonify, send_file
import os
import requests
# from pytube import YouTube

app = Flask(__name__)

# Ensure you have a directory to save the downloaded videos
if not os.path.exists('downloads'):
    os.makedirs('downloads')

@app.route('/convert', methods=['POST'])
def convert_video():
    data = request.get_json()
    url = data['url']
    
    try:
        # Here, you would integrate with a service or library that downloads and converts the YouTube video.
        # For example, using pytube (commented out because it's just a placeholder):
        # yt = YouTube(url)
        # stream = yt.streams.filter(file_extension='mp4').first()
        # file_path = stream.download(output_path='downloads')
        
        # Simulate a file download for the example
        file_path = 'downloads/sample.mp4'
        
        download_url = f"/download/{os.path.basename(file_path)}"
        return jsonify({'success': True, 'downloadUrl': download_url})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join('downloads', filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
