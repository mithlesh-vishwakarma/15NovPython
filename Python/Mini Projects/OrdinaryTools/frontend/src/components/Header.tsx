interface Props {
  tagline?: string;
}

export default function Header({ 
  tagline = "THE ULTIMATE MEDIA TOOLKIT"
}: Props) {
  return (
    <header className="header" id="header">
      <div className="container">
        <div className="header__brand-row">
          <div className="header__brand">
            <div className="header__logo-text">&lt; OrdinaryTools /&gt;</div>
            <div className="logo-subtitle">{tagline}</div>
          </div>
        </div>
      </div>
    </header>
  );
}
