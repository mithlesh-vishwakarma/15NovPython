import { useState, useCallback } from "react";
import type { VideoInfo, AppState } from "./types";
import { fetchVideoInfo, downloadVideo, triggerBrowserDownload } from "./api";

import Header from "./components/Header";
import UrlInput from "./components/UrlInput";
import VideoPreview from "./components/VideoPreview";
import FormatTable from "./components/FormatTable";
import DownloadProgress from "./components/DownloadProgress";
import ErrorBanner from "./components/ErrorBanner";
import Footer from "./components/Footer";

export default function App() {
  const [appState, setAppState] = useState<AppState>("idle");
  const [videoInfo, setVideoInfo] = useState<VideoInfo | null>(null);
  const [currentUrl, setCurrentUrl] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [downloadProgress, setDownloadProgress] = useState(-1);
  const [downloadingFormatId, setDownloadingFormatId] = useState<string | null>(
    null
  );

  // --- Fetch video info ---
  const handleFetch = useCallback(async (url: string) => {
    setAppState("fetching");
    setErrorMessage("");
    setVideoInfo(null);
    setCurrentUrl(url);

    try {
      const info = await fetchVideoInfo(url);
      setVideoInfo(info);
      setAppState("ready");
    } catch (err) {
      setErrorMessage(
        err instanceof Error ? err.message : "Failed to fetch video info"
      );
      setAppState("error");
    }
  }, []);

  // --- Download a format ---
  const handleDownload = useCallback(
    async (formatId: string) => {
      if (!currentUrl) return;

      setAppState("downloading");
      setDownloadingFormatId(formatId);
      setDownloadProgress(-1);
      setErrorMessage("");

      try {
        const { blob, filename } = await downloadVideo(
          currentUrl,
          formatId,
          (loaded, total) => {
            setDownloadProgress((loaded / total) * 100);
          }
        );

        triggerBrowserDownload(blob, filename);
        setAppState("ready");
      } catch (err) {
        setErrorMessage(
          err instanceof Error ? err.message : "Download failed"
        );
        setAppState("error");
      } finally {
        setDownloadingFormatId(null);
        setDownloadProgress(-1);
      }
    },
    [currentUrl]
  );

  const dismissError = () => {
    setErrorMessage("");
    if (videoInfo) {
      setAppState("ready");
    } else {
      setAppState("idle");
    }
  };

  return (
    <>
      <Header />

      <UrlInput onFetch={handleFetch} isLoading={appState === "fetching"} />

      {errorMessage && (
        <ErrorBanner message={errorMessage} onDismiss={dismissError} />
      )}

      {appState === "downloading" && (
        <DownloadProgress progress={downloadProgress} />
      )}

      {videoInfo && (
        <>
          <VideoPreview video={videoInfo} />
          <FormatTable
            formats={videoInfo.formats}
            onDownload={handleDownload}
            isDownloading={appState === "downloading"}
            downloadingFormatId={downloadingFormatId}
          />
        </>
      )}

      <Footer />
    </>
  );
}
