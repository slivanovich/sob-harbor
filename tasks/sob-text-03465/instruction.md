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
George W. Bernard: Professor George W. Bernard is a British historian who specializes in the reign of King Henry VIII, specifically the English Reformation of the 1530s – both in England and globally – and the 'reign' of Anne Boleyn.  He is most famous for his arguments for the strength of Henry VIII as a ruler not controlled by faction, and for his theory that Anne Boleyn was guilty of adultery in 1536 based on a poem by Lancelot de Carles.  He is commonly pitted up against David Starkey and Eric Ives who forcefully present the opposite argument.

United States presidential debates, 2000: The United States presidential election debates were held during the 2000 presidential elections.  Three debates were held between Republican candidate, Texas Governor George W. Bush and Democratic incumbent Vice President Al Gore, the major candidates.  One debate was held with their vice presidential running mates, Dick Cheney and Joe Lieberman.  All four debates were sponsored by the non-profit Commission on Presidential Debates (CPD), which has organized presidential debates since its establishment in 1987.

David Starkey: David Robert Starkey CBE FSA RHistS (born 3 January 1945) is an English constitutional historian and a radio and television presenter.

History vs. Hollywood: History vs. Hollywood was a television show on the History Channel in the United States.  On the show, experts are interviewed on the historical accuracy of a film that is based on a historical event.  For example, the movie "The Last Samurai" was featured in one episode in which military historian Geoffrey Wawro, professor of history at the University of North Texas, and director of the university's Barsanti Military History Center, compared the movie with the actual events (December 2003).  On the show the expert guests discuss the factual accuracy of the film as well as the everyday objects that a person of the particular time period would have seen.  In some episodes an expert or the host will go on a journey to the actual historical sites depicted in the film, or interview someone who witnessed the event firsthand.  In each of the more than dozen episodes both expert guests and filmmakers will discuss the historical accuracy of the film dramatized.

Jonathan Elliot (historian): Jonathan Elliot (1784–1846) was a 19th-century American historian who produced two influential collections of documents connected with the early American republic.  The first was a five-volume collection entitled "The Debates in the Several State Conventions on the Adoption of the Federal Constitution" (commonly called "Elliot's Debates"), which encompassed the time between the 1787 Constitutional Convention and the opening of the government under the newly ratified constitution in 1789.  This work for many years was the most complete source of primary material from this period.  It was first published between 1827 and 1830, and issued in a revised version in 1861 after Elliot's death.  It has long been criticized for its haphazard and biased editing, and it has been rendered obsolete by the "Documentary History of the Ratification of the Constitution and the Bill of Rights, 1787-1791," launched in 1976 by the historian Merrill Jensen and continued by his students John P. Kaminski, Gaspare J. Saladino, Richard Leffler, and Charles Schoenleber.

Revolutionary breach of legal continuity: Revolutionary breach of legal continuity is a concept in English constitutional law, which rationalises the historic English behaviour when one King (or regime) was deposed and a de facto ruler was recognised as the new de jure monarch (or republican authority).  More generally it is any process, unauthorised by an existing legal order, which results in the creation of a new legal order; whether or not the revolutionary change is brought about by violence.  A technical breach of continuity might happen when the former constitutional arrangement is so inefficient that there isn't even a practical legal way to amend it.

United States presidential debates, 2004: The United States presidential election debates were held in the 2004 presidential elections.  Three debates were held between Republican incumbent George W. Bush and Democratic candidate John Kerry, the major candidates, and one debate was held with their vice presidential running mates, incumbent Dick Cheney and John Edwards.  All four debates were sponsored by the non-profit Commission on Presidential Debates (CPD), which has organized presidential debates since its establishment in 1987.

We Were There: The We Were There books are a series of historical novels written for children.  The series consists of 36 titles, first released between 1955 and 1963 by Grosset & Dunlap.  Each book in the series is a fictional retelling of an historical event, featuring one or more children as primary characters.  The books were written by a number of different authors, each writing from one to seven of the books; the authors included Benjamin Appel, Jim Kjelgaard, Earl Schenck Miers, William O. Steele, and others.  Each book's byline also lists a separate "historical consultant," who was a specialist in the historic topic covered by that particular book.  The historical consultants were typically college professors or, in the case of war-related stories, retired military officers; among the more noteworthy consultants for the series were the historians Bruce Catton, Walter Prescott Webb and A. B. Guthrie, Jr..  The books are illustrated with black-and-white line art, with color drawings on the dust jacket.

George Edwards (marching band director): Professor George W. Edwards (November 5, 1948 – May 28, 2009) was the director of bands for Prairie View A&M University.

Reel to Real (U.S. TV series): Reel to Real is an American television series on the History channel, hosted by Steve Gillon.  "Reel to Real" shows a film based on a historical event, paired with a documentary about that same historical event.  Historians debate the historical correctness of the film during the intermission.  Films that have appeared on "Reel to Real" include "Battle of the Bulge", "Braveheart", "The Siege", "Bat 21", "Escape from Alcatraz", "The Last of the Mohicans", "Glory", "Unforgiven", "JFK", "Pearl Harbor", "Tobruk", "Pale Rider", "The Outlaw Josey Wales".

Question: Professor George W. Bernard typically debates with an English constitutional historian about which historical event?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "first_historian": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "specialization": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "specialization"
      ],
      "additionalProperties": false
    },
    "second_historian": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "profession": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "profession"
      ],
      "additionalProperties": false
    },
    "debated_historical_event": {
      "type": "string"
    },
    "specific_debated_topics": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "first_historian",
    "second_historian",
    "debated_historical_event",
    "specific_debated_topics"
  ],
  "additionalProperties": false
}
