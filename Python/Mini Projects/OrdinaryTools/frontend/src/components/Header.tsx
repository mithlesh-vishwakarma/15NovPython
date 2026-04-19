interface Props {
  tagline?: string;
  onNavigate?: (page: any) => void;
}

export default function Header({ 
  tagline = "THE ULTIMATE MEDIA TOOLKIT",
  onNavigate
}: Props) {
  const handleNav = (e: React.MouseEvent, page: string) => {
    e.preventDefault();
    if (onNavigate) onNavigate(page);
  };

  return (
    <header className="header" id="header">
      <div className="container">
        <nav className="header__nav">
          <div className="header__left">
            <div className="header__brand" style={{ cursor: 'pointer' }} onClick={(e) => handleNav(e, 'home')}>
              <div className="header__logo-text">&lt; OrdinaryTools /&gt;</div>
              <div className="logo-subtitle">{tagline}</div>
            </div>
          </div>

          <div className="header__center">
            <div className="header__menu">
              <a href="#" className="header__menu-link" onClick={(e) => handleNav(e, 'home')}>Tools</a>
              <a href="#" className="header__menu-link" onClick={(e) => handleNav(e, 'coming-soon')}>Mocks</a>
              <a href="#" className="header__menu-link" onClick={(e) => handleNav(e, 'coming-soon')}>Password Generator</a>
            </div>
          </div>

          <div className="header__right">
            <button className="btn btn--primary btn--small">
              LogIn / SignUp
            </button>
          </div>
        </nav>
      </div>
    </header>
  );
}
