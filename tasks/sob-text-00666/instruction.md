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
IPhone OS 1: iPhone OS 1 is the first major release of iOS, Apple's mobile operating system.  iPhone OS 1.1.5 is the latest and the last version of Apple's iPhone OS 1.  This version of iOS was the first iteration of the touch-centric mobile operating system.  No official name was given on its initial release; Apple marketing literature simply stated that the iPhone runs a version of Apple's desktop operating system, macOS, then known as OS X. On March 6, 2008, with the release of the iPhone software development kit (iPhone SDK), Apple named it "iPhone OS" (they later went on to rename it "iOS" on June 7, 2010).

A-10 Cuba!: A-10 Cuba!  is a flight simulator computer game released by Parsoft Interactive in 1996 for Windows and Mac.  The game was a sequel to the Mac-exclusive "A-10 Attack! ".

Extension conflict: Extension conflicts were sometimes a problem on Apple Macintosh computers running the classic Mac OS, especially System 7.  Extensions were bundles of code that extended the operating system's capabilities by directly patching OS calls, thus receiving control instead of the operating system when applications (including the Finder) made system calls.  Generally, once an extension had done what it wanted, it was supposed to pass on the (possibly modified) system call to the operating system's routine.  If multiple extensions want to patch the same system call, they end up receiving the call in a chain, the first extension in line passing it on to the next, and so on, until the last extension passes to the operating system.  If an extension does not hand the next extension in line what it is expecting, bad things result, ranging from unexpected behavior to full system crashes.

Classic Mac OS: The "Classic" Mac OS is a graphical user interface-based operating system developed by Apple Inc. for its Macintosh family of personal computers from 1984 until 2001, the original member of the series of Macintosh operating systems.  The Macintosh platform, which was introduced in the classic Mac OS, is credited with having popularized the early GUI concept.  Mac OS was preinstalled on every Macintosh computer that was made during the era it was developed; it was also sold separately in retail stores.

MacOS version history: The history of macOS, Apple's current Mac operating system originally named Mac OS X until 2012 and then OS X until 2016, began with the company's project to replace its "classic" Mac OS.  That system, up to and including its final release Mac OS 9, was a direct descendant of the operating system Apple had used in its Macintosh computers since their introduction in 1984.  However, the current macOS is a Unix operating system built on technology that had been developed at NeXT from the 1980s until Apple purchased the company in early 1997.

Operating System Projects: OSP, an Environment for Operating System Projects, is a teaching operating system designed to provide an environment for an introductory course in operating systems.  By selectively omitting specific modules of the operating system and having the students re-implement the missing functionality, an instructor can generate projects that require students to understand fundamental operating system concepts.

Parsoft Interactive: Parsoft Interactive, or simply Parsoft, is a former computer game company known for their series of technically advanced combat flight simulators.  The name comes from Eric Parker, founder and chief developer.  Their first release was "Hellcats Over the Pacific" on the Apple Macintosh in 1991, which they followed in 1992 with "Missions at Leyte Gulf", an expansion pack.  In 1995 they released "A-10 Attack! " to critical acclaim on the Mac, following that up with "A-10 Cuba" in 1996.  Partnering with Activision, "A-10 Cuba" was also released as a stand-alone game for Microsoft Windows, and this partnership led to the Windows-only 1999 release of "" (SDoE).  The pressure of the SDoE release led to the programmers going their separate ways, and by 2002 the company was dissolved.

List of mergers and acquisitions by Apple: Apple Inc. is an American multinational corporation that designs and manufactures consumer electronics and software products.  It was established in Cupertino, California, on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne, and was incorporated on January 3, 1977.  The company's hardware products include the Macintosh line of personal computers, the iPod line of portable media players, the iPad line of tablets, the iPhone line of smartphones, the Apple TV line of digital media players, and the Apple Watch line of smartwatches.  Apple's software products include the OS X operating system, the iOS mobile operating system, the tvOS operating system, the watchOS operating system, the iTunes media browser, and the iLife suite of multimedia and creativity software.  As of 2017 , Apple is publicly known to have acquired 70 companies.  The actual number of acquisitions is possibly larger as Apple does not reveal the majority of its acquisitions unless discovered by journals.  Apple has also purchased stakes in two companies, as well as made two divestments. Apple has not released the financial details for the majority of its mergers and acquisitions.

A-10 Attack!: A-10 Attack!  is a combat flight simulator for the Apple Macintosh computer released by Parsoft Interactive in 1995.  The game features an A-10 Thunderbolt II aircraft that takes part in a variety of missions in West Germany during a hypothetical limited conventional attack by the Warsaw Pact.  A-10 boasted one of the most detailed flight models of any game of its era, a physics model that extended to solid-body interactions with the ground and complete aerodynamics for every object in the game, including ordnance.  Macworld rated it "Best Flight Simulator" in a review of Mac simulations.

OS/360 Object File Format: The OS/360 Object File Format is the standard object module file format for the IBM DOS/360, OS/360 and VM/370, Univac VS/9, and Fujitsu BS2000 mainframe operating systems.  In the 1990s, the format was given an extension with the XSD-type record for the MVS Operating System to support longer module names in the C Programming Language.  This format is still in use by the z/VSE operating system (the follow-on to the DOS/360 Operating System).  In contrast, it has been superseded by the GOFF file format on the MVS Operating System (the follow-on to the OS/360 Operating System) and on the z/VM Operating System (the follow-on to the VM/370 Operating System).  Since the MVS and z/VM loaders will still handle this older format, some compilers have chosen to continue to produce this format instead of the newer GOFF format.

Question: Which Apple operating system did the game that was a sequel to the Mac-exclusive "A-10 Attack!" require?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_name": {
      "type": "string",
      "description": "The name of the game that is the sequel."
    },
    "game_release_year": {
      "type": "integer",
      "description": "The year the game was released."
    },
    "required_operating_system": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the Apple operating system required by the game."
        },
        "developer": {
          "type": "string",
          "description": "The developer of the operating system."
        },
        "type": {
          "type": "string",
          "description": "A description of the operating system's interface type."
        },
        "development_period": {
          "type": "object",
          "properties": {
            "start_year": {
              "type": "integer",
              "description": "The start year of the operating system's development period."
            },
            "end_year": {
              "type": "integer",
              "description": "The end year of the operating system's development period."
            }
          },
          "required": [
            "start_year",
            "end_year"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "developer",
        "type",
        "development_period"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "game_name",
    "game_release_year",
    "required_operating_system"
  ],
  "additionalProperties": false
}
