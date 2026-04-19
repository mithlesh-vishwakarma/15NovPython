export default function Footer() {
  return (
    <footer className="footer" id="footer">
      <div className="container">
        <p className="footer__text">
          Built with React, TypeScript & FastAPI — Powered by{" "}
          <a
            href="https://github.com/yt-dlp/yt-dlp"
            target="_blank"
            rel="noopener noreferrer"
          >
            yt-dlp
          </a>
        </p>
        <p className="footer__disclaimer">
          ⚠️ This tool is for educational purposes only. Downloading copyrighted
          content without permission may violate YouTube's Terms of Service and
          applicable laws. Use responsibly.
        </p>
      </div>
    </footer>
  );
}
