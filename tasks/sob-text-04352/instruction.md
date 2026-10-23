{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nUncyclopedia: Uncyclopedia is a satirical website that parodies Wikipedia.  Its logo, a hollow \"puzzle potato\", parodies Wikipedia's globe puzzle logo, and it styles itself \"the content-free encyclopedia\", parodying Wikipedia's slogan of \"the free encyclopedia\".  Founded in 2005 as an English-language wiki, the project spans over 75 languages.  The English version has approximately 30,000 pages of content, second only to the Portuguese.\n\nAndrew Schlafly: Andrew Layton \"Andy\" Schlafly ( ; born April 27, 1961) is an American lawyer and Christian conservative activist, and the founder and owner of the wiki Conservapedia.  He is the son of the conservative activist and lawyer Phyllis Schlafly.\n\nWiki journalism: Wiki journalism is a form of participatory journalism or crowdsourcing, which uses wiki technology to facilitate collaboration between users.  It is a kind of collaborative journalism.  The largest example of wiki journalism is Wikinews.  According to Paul Bradshaw, there are five broad types of wiki journalism: second draft wiki journalism, a ‘second stage’ piece of journalism, during which readers can edit an article produced in-house; crowdsourcing wiki journalism, a means of covering material which could not have been produced in-house (probably for logistical reasons), but which becomes possible through wiki technology; supplementary wiki journalism, creating a supplement to a piece of original journalism, e.g. a tab to a story that says \"Create a wiki for related stories\"; open wiki journalism, in which a wiki is created as an open space, whose subject matter is decided by the user, and where material may be produced that would not otherwise have been commissioned; and logistical wiki journalism, involving a wiki limited to in-house contributors which enables multiple authorship, and may also facilitate transparency, and/or an\n\nGanfyd: Ganfyd is a medical wiki community and online medical wiki encyclopedia, created in November 2005 by a group of doctors working in the United Kingdom.  The site has been the subject of academic exposition into emerging methods of disseminating medical information and more specifically, the restricting of editors within an open collaborative wiki environment.  This model has subsequently been copied by other medical wikis, but some attempts to improve on the model, such as Medpedia have failed.  In 2010, Paula Younger noted it as a laudable attempt to make medical information freely accessible and authoritative.\n\nConservapedia: Conservapedia is an English-language wiki encyclopedia project written from an American conservative point of view.  The website was started in 2006 by American homeschool teacher and attorney Andrew Schlafly, son of conservative activist Phyllis Schlafly, to counter what he perceived as a liberal bias present in Wikipedia.  It uses editorials and a wiki-based system to generate content.\n\nThe Wiki Way: The Wiki Way: Quick Collaboration on the Web is a 2001 book about wikis by Bo Leuf and Ward Cunningham.  It was the first major book published about using wikis.  Cunningham is the inventor of wikis, having created WikiWikiWeb, the first wiki website software.  The book is about how to install/customize/manage wiki systems, followed by a perspective on the nature of wiki-style online communication.\n\nWiktionary: Wiktionary is a multilingual, web-based project to create a free content dictionary of all words in all languages.  It is collaboratively edited via a wiki, and its name is a portmanteau of the words \"wiki\" and \"dictionary\".  It is available in 171 languages and in Simple English.  Like its sister project Wikipedia, Wiktionary is run by the Wikimedia Foundation, and is written collaboratively by volunteers, dubbed \"Wiktionarians\".  Its wiki software, MediaWiki, allows almost anyone with access to the website to create and edit entries.\n\nAboutUs.com: AboutUs.com is a wiki Internet domain directory.  It listed websites along with information about their content.  As a wiki, AboutUs allows Internet users to add entries or modify information.  AboutUs.com has since become a wiki for more than just websites.  The site now allows pages to be created for people, places, and almost anything else.\n\nWikidot: Wikidot Inc. is a Polish wiki hosting corporation which owns, operates and supports the community of wiki-based web projects at Wikidot.com, a social networking service and wiki hosting service (or wiki farm), developed in Toruń, Poland.  Wikidot.com was launched on August 1, 2006 and in 2009 it was the world's third-largest wiki farm, with 570,000 users running 150,000 sites with 5.6 million pages of user-created content (as of September 24, 2010).  Wikidot.com grows by about 900-1,000 new users each day.  Wikidot.com roughly doubled in size during 2011.  Following their migration to Amazon Web Services in September 2012, Wikidot became a finalist and first prize winner in the AWS Global Start-Up Challenge of 2012 under the category of Consumer Applications.  Wikidot Inc. released Wikidot.org in January 2008, the official FOSS version of the Wikidot.com software project with an Ajax-based interface.  It is meant as a stable and free software for a single Wiki install or a Wiki farm on a GNU/Linux computer.  The FOSS Wikidot.org software is licensed under the GNU Affero General Public License.  There are Debian/Ubuntu (*. deb) packages for the free Wikidot.org software, which are considered experimental, as of October 2011, and may break existing Wikidot installations.  Wikidot Inc. is incorporated in Delaware, USA, Division of Corporations, file no. 4326793.\n\nSusning.nu: Susning.nu was a Swedish language wiki, started in October 2001 by Lars Aronsson (also the founder of Project Runeberg).  In its first three years (2001–2004), Susning.nu ran as an open wiki that anyone could edit.  Susning didn't have a pronounced ambition and could perhaps be compared in scope to Everything2; Aronsson's stated original aim for Susning was \"to make it into whatever the users want it to be\".  As such, Susning was an encyclopedia, a dictionary, and a discussion forum about any concept of interest to its users.  Because of this, Susning grew and became Sweden's biggest and the world's next biggest wiki.  In April 2004, Susning had over 60,000 articles on various topics, which was more than any other Swedish wiki at that time.  During its first few years it was in direct competition with the Swedish Wikipedia.  However, because of the website's popularity, Susning was highly affected by vandals.  In attempt at preventing vandalism, many efforts were made by Susning's founder Lars Aronsson, which were mostly unsuccessful.  Users who regularly edited at Susning were called \"susare\".\n\nQuestion: Who is the mother of the man who created the English-language wiki encycopedia project?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"project_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of wiki project mentioned.\"\n    },\n    \"project_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the specific wiki project.\"\n    },\n    \"project_language\": {\n      \"type\": \"string\",\n      \"description\": \"The primary language of the wiki project.\"\n    },\n    \"founder_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the founder of the project.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the person in relation to the project (e.g., founder, creator).\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"mother_of_founder\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the mother of the project's founder.\"\n    }\n  },\n  \"required\": [\n    \"project_type\",\n    \"project_name\",\n    \"project_language\",\n    \"founder_details\",\n    \"mother_of_founder\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "project_type": {
        "type": "string",
        "description": "The type of wiki project mentioned."
      },
      "project_name": {
        "type": "string",
        "description": "The name of the specific wiki project."
      },
      "project_language": {
        "type": "string",
        "description": "The primary language of the wiki project."
      },
      "founder_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the founder of the project."
          },
          "role": {
            "type": "string",
            "description": "The role of the person in relation to the project (e.g., founder, creator)."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      },
      "mother_of_founder": {
        "type": "string",
        "description": "The name of the mother of the project's founder."
      }
    },
    "required": [
      "project_type",
      "project_name",
      "project_language",
      "founder_details",
      "mother_of_founder"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
