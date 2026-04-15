export default function Header() {
  return (
    <header className="header" id="header">
      <div className="container">
        <div className="header__logo">
          <div className="header__icon" aria-hidden="true">▶</div>
          <h1 className="header__title">YTGrab</h1>
        </div>
        <p className="header__subtitle">
          Paste a YouTube link, pick your quality, and download instantly.
        </p>
      </div>
    </header>
  );
}
