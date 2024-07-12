{ pkgs }: 
pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.chromium
    pkgs.chromedriver
    pkgs.python3Packages.selenium
  ];
}