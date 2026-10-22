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
Richard Ruppel: Richard J. Ruppel is a professor in and chair of the English Department at Viterbo University in La Crosse, Wisconsin.  A notable scholar on Joseph Conrad and sexuality, he has edited, with Philip Holden, a collection of essays entitled "Imperial Desire: Dissident Sexualities and Colonial Literature", while his own essays on Conrad have been published in such journals as "Conradiana", "The Conradian", "Studies in the Novel" and "L'Epoque Conradienne".  As of 1998, he was in the throes of work on a book about male intimacy in the life and works of Conrad.

The Nature of a Crime: The Nature of a Crime is a collaborative novel written and published in 1909 by authors Joseph Conrad and Ford Madox Ford.  The text did not acquire acclaim until after Conrad's death in 1924, when Ford brought the text to light in his essay "".  "The Nature of a Crime" is the last of three books written by Conrad and Ford.

Re-Edition Texts: Heart of Darkness: Re-Editioned Texts: Heart of Darkness is a novel by Stephanie Syjuco, with 12 reproduced versions of Joseph Conrad's novel "Heart of Darkness".  Each version of the novel includes Joseph Conrad's "Heart of Darkness" opened in different online sources and printed without any changes.  Each version is unique to the other 11.  Differences include Font size, Font type, advertisements, and even mistakes.

Peters, Fraser &amp; Dunlop: Peters Fraser and Dunlop (PFD) is a talent and literary agency based in London, England.  One of the oldest agencies in Britain, and a co-founder of the Association of Authors' Agents, it is home to a distinguished and varied client list, including Jeanette Winterson, Ruby Wax, Steve Peters, Helen Rappaport, Simon Schama, William Hague, Sarah Raven, Twiggy, Sir Max Hastings, Chris Patten, Bear Grylls, Valentine Warner, Philip Norman and such estates as V.S. Pritchett, E.M. Forster, Georges Simenon, Margery Allingham C.S. Forester, Robert Bolt, Edmund Crispin and Storm Jameson.

Franz Conrad von Hötzendorf: "K.u.k. Feldmarschall" Franz Xaver Joseph Conrad Graf von Hötzendorf German: "Franz Xaver Josef Graf Conrad von Hötzendorf" (11 November 1852 – 25 August 1925), sometimes anglicised as Hoetzendorf, was an Austrian Field Marshal and Chief of the General Staff of the armed forces of the Austro-Hungarian Army and Navy 1906–1917.  He was the Empire's chief of staff during the 1914 July Crisis that led to the outbreak of World War I.  He argued persuasively for preventive war against Serbia, saying it was needed to hold together his polyglot empire on the verge of breaking down.  He later decided that Austria acted too late, and its failure to fight earlier was a fatal mistake.  He admitted his army was not ready for war, and therefore emphasized the political necessity.  He failed to realize that Germany would force him to put his chief assets on the Russian front, rather than Serbia.  Conrad was fearful of attacking Russia and when Russia nearly broke through the Carpathian mountains and Conrad's Carpathian Offensive failed Italy entered the war thinking the Empire was collapsing.  It was not a good time however as Germany helped Austria break through Russia and the taking of Serbia so Conrad shifted his attention away from the Balkans toward Italy and Russia.  From early 1915 his forces were increasingly dependent on German support and command.  Without German support the Austrian army was a spent force.

Victory (novel): Victory (also published as Victory: An Island Tale) is a psychological novel by Joseph Conrad first published in 1915, through which Conrad achieved "popular success."  The "New York Times", however, called it "an uneven book" and "more open to criticism than most of Mr. Conrad's best work."

Joseph Conrad: Joseph Conrad (] ; born Józef Teodor Konrad Korzeniowski; 3 December 1857 – 3 August 1924) was a Polish-British writer regarded as one of the greatest novelists to write in the English language.  He joined the British merchant marine in 1878, and was granted British nationality in 1886.  Though he did not speak English fluently until his twenties, he was a master prose stylist who brought a non-English sensibility into English literature.  He wrote stories and novels, many with a nautical setting, that depict trials of the human spirit in the midst of an impassive, inscrutable universe.

Under Western Eyes (novel): Under Western Eyes (1911) is a novel by Joseph Conrad.  The novel takes place in St. Petersburg, Russia, and Geneva, Switzerland, and is viewed as Conrad's response to the themes explored in "Crime and Punishment"; Conrad was reputed to have detested Dostoevsky.  It is also, some say, Conrad's response to his own early life; his father was a famous revolutionary imprisoned by the Russians, but, instead of following in his father's footsteps, at the age of sixteen Conrad left his native land forever.  Indeed, while writing "Under Western Eyes", Conrad suffered a weeks-long breakdown during which he conversed with the novel's characters in Polish.

Storm Jameson: Margaret Storm Jameson (8 January 1891 – 30 September 1986) was an English journalist and author, known for her novels and reviews.

Jess Conrad: Jess Conrad OBE (born Gerald Arthur James on 24 February 1936) is an actor and singer from Britain.  As a boy he was nicknamed "Jesse" after American outlaw Jesse James; as there was already an actor named "Gerald James" in Actors' Equity, a drama teacher who was a fan of Joseph Conrad suggested the stage name of "Jess Conrad".

Question: Were Margaret Storm Jameson and Joseph Conrad both known for their reviews?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "answer": {
      "type": "boolean",
      "description": "True if both individuals were known for reviews, false otherwise."
    },
    "individuals_involved": {
      "type": "array",
      "description": "Details about each individual mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the individual."
          },
          "known_for_reviews": {
            "type": "boolean",
            "description": "Indicates if the individual was known for their reviews based on the context."
          },
          "primary_known_for": {
            "type": "string",
            "description": "A description of what the individual was primarily known for, as per the context."
          }
        },
        "required": [
          "name",
          "known_for_reviews",
          "primary_known_for"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "question_asked",
    "answer",
    "individuals_involved"
  ],
  "additionalProperties": false
}
