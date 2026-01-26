[Setup]
AppName=HdW Flyer Creator
#define MyAppVersion GetEnv("VERSION")
AppVersion={#MyAppVersion}
OutputBaseFilename=FlyerCreator_{#MyAppVersion}_Setup
DefaultGroupName=Haus der Wissenschaft
SetupIconFile=rsc\icons\app.ico
Compression=lzma
SolidCompression=yes
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
DefaultDirName={code:GetInstallDir}

[Files]
Source: "dist\launch\*"; \
  DestDir: "{app}"; \
  Excludes: "rsc\*"; \
  Flags: recursesubdirs createallsubdirs
Source: "dist\launch/_internal\rsc\*"; \
  DestDir: "{userappdata}\HausDerWissenschaft\rsc"; \
  Flags: recursesubdirs createallsubdirs

[Dirs]
Name: "{userappdata}\HausDerWissenschaft"; Flags: uninsneveruninstall

[Icons]
Name: "{group}\Flyer Creator"; Filename: "{app}\launch.exe"
Name: "{code:GetDesktopDir}\Flyer Creator"; Filename: "{app}\launch.exe"; Tasks: desktopicon

[Tasks]
Name: desktopicon; Description: "Desktop-Verknüpfung erstellen"; Flags: unchecked

[Code]

function GetInstallDir(Param: string): string;
begin
  if IsAdminInstallMode then
    Result := ExpandConstant('{pf}\HausDerWissenschaft')
  else
    Result := ExpandConstant('{localappdata}\Programs\HausDerWissenschaft');
end;

function GetDesktopDir(Param: string): string;
begin
  if IsAdminInstallMode then
    Result := ExpandConstant('{commondesktop}')
  else
    Result := ExpandConstant('{userdesktop}');
end;

