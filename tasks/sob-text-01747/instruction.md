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
Louis XIV of France: Louis XIV (5 September 16381 September 1715), known as Louis the Great ("Louis le Grand ") or the Sun King ("le Roi Soleil "), was a monarch of the House of Bourbon who reigned as King of France from 1643 until his death in 1715.  His reign of 72 years and 110 days is the longest recorded of any monarch of a sovereign country in European history.  In the age of absolutism in Europe, Louis XIV's France was a leader in the growing centralization of power.

Helmut Walser Smith: Helmut Walser Smith is Martha Rivers Ingram Professor of History at Director of the Max Kade Center for European and German Studies at Vanderbilt University.  His teaching and writing focus on modern German history, especially the long nineteenth century.  He has served on the editorial boards of Central European History and the Journal of Modern History and in 2011-12 is President of the Conference Group on Central European History of the American Historical Association.  From 2005-2008, he was Director of the Robert Penn Warren Center for the Humanities at Vanderbilt.

Recensio.net: recensio.net – review platform for European history – is a Europe-wide, multi-language platform for scholarly reviews of historical literature.  Launched in January 2011, the platform is operated by three institutions: the Bavarian State Library in Munich, the German Historical Institute Paris, and the Institute of European History in Mainz.  It has been described by the media as an attempt of historians to "venture into the Web 2.0".

William W. Hagen: William W. Hagen (born 1942) is a prominent historian and Professor of History at the University of California-Davis.  Hagen's focus is on Modern European History, primarily in relation to Germany and Eastern Europe.  He obtained his B.A. from Harvard University and his M.A. and Ph.D. from the University of Chicago.  Starting as Assistant Professor in 1970,  he became Associate Professor of History in 1977 and Professor of History in 1981.  From 1992-1998, Hagen served as Director of the "UC Davis Center for History, Society, and Culture".  In 1996, he served as President of the "Conference Group for Central European History" (American Historical Association).

David Blackbourn: David Gordon Blackbourn (born 1949 in Yorkshire, England) is Cornelius Vanderbilt Distinguished Chair of History at Vanderbilt University, where he teaches modern German and European history.  Prior to arriving at Vanderbilt, Blackbourn was Coolidge Professor of History at Harvard University and served as director of the university's Minda de Gunzburg Center for European Studies from 2007-2012.  He is on the editorial board of the journal "Past & Present"; the academic advisory board of the Institute for European History, Mainz; and the advisory board of the Friends of the German Historical Institute, Washington.  He was chair of the Harvard History Department in 1998–1999 and 2000–2002, and was president of the Conference Group on Central European History of the American Historical Association (since 2012 called Central European History Society) in 2003–2004.

AP European History: Advanced Placement European History (commonly known as AP Modern European History, AP Euro, AP European, or APEH), is a course and examination offered by the College Board through the Advanced Placement Program.  This course is for high school students who are interested in a first year university level course in European history.  The course surveys European history from between 1300-1450 CE to the present, focusing on religious, social, economic, and political themes.  In the United States, the course is usually taken in sophomore year of high school.

House of European History: The House of European History (HEH) is a museum in Brussels, Belgium that focuses on the history of Europe since 1789.  It is an initiative by the European Parliament and opened on 6 May 2017.  As a cultural institution and exhibition centre, the House of European History intends to promote the understanding of European history and European integration, through a permanent exhibition and temporary and travelling exhibitions.

Central European History: Central European History is a peer-reviewed academic journal on history published quarterly by Cambridge University Press on behalf of the Conference Group for Central European History of the American Historical Association.  It covers all aspects of central European history from the Middle Ages to the present day.  It was established in 1968 and is edited by Andrew I. Port and Julia Torrie.

Paul Jankowski: Paul Jankowski is a history professor at Brandeis University.  Jankowski has given several lectures concerning important world affairs such as the Paris riots.  He has written books about events like the Stavisky Affair.  He is the Raymond Ginger Professor of History at Brandeis University, and the former chair of the history department.  His expertise is in modern French and European history, as well as war and conflict in European history.  He did his undergraduate and doctoral work at Oxford University.

Essai sur les mœurs et l'esprit des nations: Essai sur les mœurs et l'esprit des nations ("Essay on Universal History, the Manners, and Spirit of Nations") is a work by the French writer, historian, and philosopher Voltaire, published for the first time in 1756.  It discusses the history of Europe before Charlemagne until the dawn of the age of Louis XIV, also addressing the colonies and the East.

Question: Who wrote a work that described European history until the dawn of the age of the longest serving monarch in European history?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The name of the author who wrote the work."
    },
    "work_title": {
      "type": "string",
      "description": "The title of the historical work."
    },
    "monarch_referenced": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the monarch whose age is referenced in the work's scope."
        },
        "title": {
          "type": "string",
          "description": "The primary title of the monarch."
        },
        "reign_duration_years": {
          "type": "integer",
          "description": "The duration of the monarch's reign in years."
        },
        "reign_duration_days": {
          "type": "integer",
          "description": "The additional duration of the monarch's reign in days."
        },
        "is_longest_reign_in_european_history": {
          "type": "boolean",
          "description": "Indicates if this monarch had the longest recorded reign in European history."
        }
      },
      "required": [
        "name",
        "title",
        "reign_duration_years",
        "reign_duration_days",
        "is_longest_reign_in_european_history"
      ],
      "additionalProperties": false
    },
    "work_historical_scope": {
      "type": "string",
      "description": "A description of the historical period covered by the work."
    }
  },
  "required": [
    "author_name",
    "work_title",
    "monarch_referenced",
    "work_historical_scope"
  ],
  "additionalProperties": false
}
