import Disclaimer from "./Disclaimer";

interface Props {
  title?: string;
  subtitle?: string;
  icon?: string;
}

export default function Header({ 
  title = "OrdinaryTools", 
  subtitle = "Simple, powerful tools for everyday tasks.",
  icon = "🛠️"
}: Props) {
  return (
    <header className="header" id="header">
      <div className="container">
        <div className="header__logo">
          <div className="header__icon" aria-hidden="true">{icon}</div>
          <h1 className="header__title">{title}</h1>
        </div>
        <p className="header__subtitle">
          {subtitle}
        </p>
        <Disclaimer />
      </div>
    </header>
  );
}
