Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Pegasus (spyware): Pegasus is a spy software installable on devices running certain versions of iOS, Apple's mobile operating system.  Discovered in August 2016 after a failed attempt at installing it on an iPhone belonging to a human rights defender, an investigation revealed details about the spyware, its abilities, and the security vulnerabilities it exploited.  The installation was avoided when the defender declined to use a link that was offered on the intended device.  Pegasus is capable of reading text messages, tracking calls, collecting passwords, tracing the location of the phone, and gathering information from apps, including iMessage, Gmail, Viber, Facebook, WhatsApp, and Skype.  Apple released version 9.3.5 of its software to fix the vulnerabilities.  News of the spyware garnered significant media attention.  It was called the "most sophisticated" smartphone attack ever, and became the first time in iPhone history when a remote jailbreak exploit had been detected.  The company that created the spyware, NSO Group, stated that they provide "authorized governments with technology that helps them combat terror and crime".  In the aftermath of the news, critics asserted that Apple's bug-bounty program, which rewards people for finding flaws in its software, might not have offered sufficient rewards to prevent exploits being sold on the black market, rather than being reported back to Apple.

JailbreakMe: JailbreakMe is a series of jailbreaks for Apple's iOS mobile operating system that take advantage of flaws in the Safari browser on the device, providing an immediate one-step jailbreak unlike more common jailbreaks, such as Blackra1n and redsn0w, that require plugging the device into a computer and running the jailbreaking software from the desktop.  Jailbreaking allows users to install software that is not approved by Apple on their iPod Touch, iPhone, and iPad; JailbreakMe automatically includes Cydia, a package management interface that serves as an alternative to the App Store.  Cydia Allows Installation of packages.

List of mergers and acquisitions by Apple: Apple Inc. is an American multinational corporation that designs and manufactures consumer electronics and software products.  It was established in Cupertino, California, on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne, and was incorporated on January 3, 1977.  The company's hardware products include the Macintosh line of personal computers, the iPod line of portable media players, the iPad line of tablets, the iPhone line of smartphones, the Apple TV line of digital media players, and the Apple Watch line of smartwatches.  Apple's software products include the OS X operating system, the iOS mobile operating system, the tvOS operating system, the watchOS operating system, the iTunes media browser, and the iLife suite of multimedia and creativity software.  As of 2017 , Apple is publicly known to have acquired 70 companies.  The actual number of acquisitions is possibly larger as Apple does not reveal the majority of its acquisitions unless discovered by journals.  Apple has also purchased stakes in two companies, as well as made two divestments. Apple has not released the financial details for the majority of its mergers and acquisitions.

IPad: iPad ( ) is a line of tablet computers designed, developed and marketed by Apple Inc., which run the iOS mobile operating system.  The first iPad was released on April 3, 2010; the most recent iPad models are the iPad (2017), released on March 24, 2017, and the 10.5 in and 12.9 in 2G iPad Pro released on June 13, 2017.  The user interface is built around the device's multi-touch screen, including a virtual keyboard.  All iPads can connect via Wi-Fi; some models also have cellular connectivity.

TrueOS: TrueOS (formerly PC-BSD or PCBSD) is a Unix-like, desktop-oriented operating system built upon the most recent releases of FreeBSD-CURRENT.  It aims to be easy to install by using a graphical installation program, and easy and ready-to-use immediately by providing KDE SC, Lumina, LXDE, MATE, or Xfce as the desktop environment.  It provides official binary Nvidia and Intel drivers for hardware acceleration and an optional 3D desktop interface through KWin, and Wine is ready-to-use in running of Microsoft Windows software.  TrueOS is able to run Linux software, in addition to FreeBSD Ports collection, and it has its own . txz package manager that allows users to graphically install pre-built software packages from a single download link, which is unique for BSD operating systems.

YMP File: The YMP file (file-extension . ymp) is a file used in the openSUSE operating system (based on the Linux kernel).  It is used in a feature called one-click install.  This allows a user to click a "One-Click Install" button on certain websites to automatically install software, without having to download and install the software separately.  The YMP file will open the one-click install manager which is managed by YaST.  The system will automatically add the repository containing the application, and then download and install the program.

Greenpois0n: Greenpois0n is a name shared by a series of iOS jailbreaking tools developed by Chronic Dev Team (sometimes called the Greenpois0n team) that use exploits to remove software restrictions on iPhones, iPads, iPod touches, and Apple TVs. Greenpois0n's initial release in October 2010 jailbroke iOS 4.1, and its second version in February 2011 jailbroke iOS 4.2.1 as well as iOS 4.2.6 on CDMA iPhones.  The second generation of the tool, Greenpois0n Absinthe, was developed with iPhone Dev Team members and jailbroke iOS 5.0.1 in January 2012 (providing the first jailbreak of the iPhone 4S), and a second version jailbroke iOS 5.1.1 in May 2012 (providing the first jailbreak of the third generation iPad).

SHSH blob: SHSH blob is a term for a small piece of data that is part of Apple's digital signature protocol for iOS restores and updates, designed to control the iOS versions that users can install on their iOS devices (iPhones, iPads, iPod touches, and Apple TVs), generally only allowing the newest iOS version to be installable.  Developers interested in iOS jailbreaking have made tools for working around this signature system in order to install jailbreakable older iOS versions that are no longer being signed by Apple.

Cydia: Cydia is a package manager mobile app for iOS that enables a user to find and install software packages on jailbroken iPhones, iPads and iPods.  It also refers to digital distribution platform for software on iOS accessed through Cydia software.  Most of the software packages available through Cydia are free of charge but some require purchasing.

IPhone OS 1: iPhone OS 1 is the first major release of iOS, Apple's mobile operating system.  iPhone OS 1.1.5 is the latest and the last version of Apple's iPhone OS 1.  This version of iOS was the first iteration of the touch-centric mobile operating system.  No official name was given on its initial release; Apple marketing literature simply stated that the iPhone runs a version of Apple's desktop operating system, macOS, then known as OS X. On March 6, 2008, with the release of the iPhone software development kit (iPhone SDK), Apple named it "iPhone OS" (they later went on to rename it "iOS" on June 7, 2010).

Question: JailbreakMe is a series of jailbreaks for Apple's iOS mobile operating system that take advantage of flaws in the Safari browser on the device, providing an immediate one-step jailbreak unlike more common jailbreaks, it automatically includes which package manager mobile app for iOS that enables a user to find and install software packages on jailbroken iPhones, iPads and iPods?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "jailbreak_tool_name": {
      "type": "string",
      "description": "The name of the jailbreak tool."
    },
    "package_manager_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the package manager mobile app."
        },
        "description": {
          "type": "string",
          "description": "A description of the package manager's function."
        }
      },
      "required": [
        "name",
        "description"
      ],
      "additionalProperties": false
    },
    "jailbreak_mechanism": {
      "type": "string",
      "description": "The mechanism or vulnerability exploited by the jailbreak tool."
    }
  },
  "required": [
    "jailbreak_tool_name",
    "package_manager_details",
    "jailbreak_mechanism"
  ],
  "additionalProperties": false
}
