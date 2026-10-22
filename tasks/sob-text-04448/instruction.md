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
Lenovo: Lenovo Group Ltd. or Lenovo PC International or shortened as Lenovo ( ; formerly stylized as lenovo) is a Chinese multinational technology company with headquarters in Beijing, China and Morrisville, North Carolina.  It designs, develops, manufactures and sells personal computers, tablet computers, smartphones, workstations, servers, electronic storage devices, IT management software, and smart televisions.  Since 2013, Lenovo is the world's largest personal computer vendor by unit sales.  It markets the ThinkPad line of notebook computers, IdeaPad and Yoga lines of notebook laptops, and the IdeaCentre and ThinkCentre lines of desktops.

Yong Rui: Yong Rui (Chinese: 芮勇) is the Chief Technology Officer and Senior Vice President of Lenovo Group.  He is in charge of Lenovo’s technical strategy, research and development directions, and Lenovo Research, one of Lenovo’s most important innovation engines.

Xunlei: Xunlei Limited () is a Chinese multinational technology company and an online service provider founded in 2003.  The subsidiary of Xunlei Limited, Shenzhen Xunlei Networking Technologies, Co., Ltd. () was formerly known as Sandai Technologies (Shenzhen) Inc. and changed its name to Shenzhen Xunlei Networking Technologies, Co., Ltd. in May 2005.  In April 2014, Xunlei received an investment from a Chinese electronics company Xiaomi of $200 million.  On 24 June 2014, it went public on the Nasdaq Stock Exchange, raising just shy of $88 million.

List of Mortal Kombat media: "Mortal Kombat" is a video game franchise originally developed and produced by Midway Games.  The video games are a series of fighting games and several action-adventure games which debuted in North American arcades on October 8, 1992 with the release of "Mortal Kombat", created by Ed Boon and John Tobias.  Mortal Kombat titles have been released on numerous different video game consoles, handheld game consoles, and personal computer platforms and is considered one of the best-selling video game franchises of all time with over 26 million games sold.  The games have appeared on every major video game console produced since its debut including every console created by Sony and Microsoft, every console produced by Sega since the Sega Genesis (as well as the Master System in Europe and South America), and every console produced by Nintendo since the Super NES.

CT510: The CT510 (previously known as the iSec and eBox) is a video game console created by eedoo Technology, a company created by Lenovo, with 40 Lenovo employees and investment of an undisclosed sum of money from the Lenovo Group, Legend Holdings and Legend Capital.  It was first announced on August 30, 2010 to be marketed in China only upon its release, with further releases in the Asian-Pacific and worldwide markets planned if the console proves to be successful.  The console was released in April 2012.

Legend Holdings: Legend Holdings Corporation () is a Chinese investment holding company with interests in finance, real estate, and information technology, and the controlling shareholder of its better-known subsidiary, the Lenovo Group.  Formed by the Chinese Academy of Sciences, Lenovo was originally Legend Computer, until the English name was changed in 2004.  Its Chinese name however remains the same, 联想 (  ).

Chinese Academy of Sciences: The Chinese Academy of Sciences (CAS; ), with historical origins in the Academia Sinica during the Republic of China era, is the national academy for the natural sciences of the People's Republic of China (PRC).  Collectively known as the "Two Academies (两院)" along with the Chinese Academy of Engineering, it is an institution of China, functioning as the national scientific think tank and academic governing body, providing advisory and appraisal services on issues stemming from the national economy, social development, and science and technology progress.  It is headquartered in Beijing, with branch institutes all over mainland China.  It has also created hundreds of commercial enterprises, Lenovo being one of the most famous.

Smartisan: Smartisan Technology Co., Ltd. (), commonly known as Smartisan, is a Chinese multinational technology company headquartered in Beijing.  It designs and markets consumer electronic devices and online services.  Its hardware product line includes the Smartisan smartphone and the Smartisan earphone.  Its consumer software include the Smartisan OS operating system.  Its online services include the Smartisan Store, the Smartisan OS App Store and Smiling Cloud.

Morrisville, North Carolina: Morrisville is a town located in both Wake and Durham counties of the U.S. state of North Carolina.  The population was 18,576 at the 2010 census.  The U.S. Census Bureau estimates the town's population to be 21,932 as of July 1, 2013.  Morrisville is part of the Research Triangle metropolitan region.  The regional name originated after the 1959 creation of the Research Triangle Park, located midway between the cities of Raleigh and Durham.  The Research Triangle region encompasses the U.S. Census Bureau's Combined Statistical Area (CSA) of Raleigh-Durham-Cary.  The estimated population of the Raleigh-Durham-Cary CSA was 1,565,223 as of July 1, 2006, with the Raleigh-Cary Metropolitan Statistical Area (MSA) portion estimated at 994,551 residents.  The U.S. headquarters of Chinese multinational Lenovo are located in the municipal limits.

DisplayLink: DisplayLink (formerly Newnham Research) is a semiconductor and software technology company.  DisplayLink USB graphics technology is designed to connect computers and displays using USB, Ethernet, and WiFi.  It also allows multiple displays to be connected to a single computer.  DisplayLink's primary customers are notebook OEMs (HP, Dell, Toshiba, Lenovo, Acer, Asus), LCD monitor manufacturers (AOC, ASUS) and PC accessory vendors (Startech.com, Targus, Belkin, Kensington, Plugable), supporting the Microsoft Windows, Mac OS X, Android, ChromeOS and Linux operating systems.

Question: The CT510 (previously known as the iSec and eBox) is a video game console created by eedoo Technology, a company created by Lenovo, Lenovo Group Ltd. or Lenovo PC International or shortened as Lenovo is a Chinese multinational technology company with headquarters in Beijing, China and which US location?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the technology company."
    },
    "company_type": {
      "type": "string",
      "description": "A description of the company's nature."
    },
    "us_headquarters": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the US headquarters is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the US headquarters is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the US headquarters is located."
        }
      },
      "required": [
        "city",
        "state",
        "country"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "company_name",
    "company_type",
    "us_headquarters"
  ],
  "additionalProperties": false
}
