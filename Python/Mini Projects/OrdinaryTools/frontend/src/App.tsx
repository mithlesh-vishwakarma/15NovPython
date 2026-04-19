import { useState } from "react";
import Home from "./pages/Home";
import YoutubeDownloader from "./pages/YoutubeDownloader";
import InstagramDownloader from "./pages/InstagramDownloader";
import Footer from "./components/Footer";

type Page = 'home' | 'youtube' | 'instagram';

export default function App() {
  const [currentPage, setCurrentPage] = useState<Page>('home');

  const navigateTo = (page: Page) => {
    setCurrentPage(page);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <>
      <main style={{ flex: 1 }}>
        {currentPage === 'home' && (
          <Home onSelect={(tool) => navigateTo(tool)} />
        )}

        {currentPage === 'youtube' && (
          <YoutubeDownloader onBack={() => navigateTo('home')} />
        )}

        {currentPage === 'instagram' && (
          <InstagramDownloader onBack={() => navigateTo('home')} />
        )}
      </main>

      <Footer />
    </>
  );
}
