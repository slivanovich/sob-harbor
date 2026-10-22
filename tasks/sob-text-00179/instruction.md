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
Pawn Sacrifice: Pawn Sacrifice is a 2014 American biographical drama film.  It is based on the true story of Bobby Fischer's challenge against top Soviet chess grandmasters during the Cold War and culminating in the 1972 World Chess Championship match versus Boris Spassky in Reykjavík, Iceland.  It was directed by Edward Zwick and written by Steven Knight.  The film stars Tobey Maguire as Bobby Fischer, Liev Schreiber as Boris Spassky, Lily Rabe as Joan Fischer, and Peter Sarsgaard as William Lombardy.  It was released in the United States on September 16, 2015.

David Hackett Fischer: David Hackett Fischer (born December 2, 1935) is University Professor and Earl Warren Professor of History at Brandeis University.  Fischer's major works have tackled everything from large macroeconomic and cultural trends ("Albion's Seed," "The Great Wave") to narrative histories of significant events ("Paul Revere's Ride," "Washington's Crossing") to explorations of historiography ("Historians' Fallacies", in which he coined the term Historian's fallacy).

Legacy of George Washington: George Washington (February 22, 1732 – December 14, 1799) commanded America's war for independence (1775–1783), and was the first President of the United States, from 1789 to 1797.  In terms of personality, a leading biographer Douglas Southall Freeman concluded, "the great big thing stamped across that man is character."  By character, says David Hackett Fischer "Freeman meant integrity, self-discipline, courage, absolute honesty, resolve, and decision, but also forbearance, decency, and respect for others."  Because of his central role in the founding of the United States, Washington is often called the "Father of his Country."  His devotion to republicanism and civic virtue made him an exemplary figure among early American politicians.  His image has become an icon and is commonplace in American culture.

Jeff Hackett: Jeffrey David Hackett (born June 1, 1968) is a Canadian former professional ice hockey goaltender who played fifteen seasons in the National Hockey League (NHL) with the New York Islanders, San Jose Sharks, Chicago Blackhawks, Montreal Canadiens, Boston Bruins and Philadelphia Flyers.  He served as the Colorado Avalanche's goaltending coach for three seasons following his playing career.

Albion's Seed: Albion's Seed: Four British Folkways in America is a 1989 book by David Hackett Fischer that details the folkways of four groups of people who moved from distinct regions of Great Britain (Albion) to the United States.  The argument is that the culture of each of the groups persisted, to provide the basis for the modern United States.  Fischer explains "the origins and stability of a social system which for two centuries has remained stubbornly democratic in its politics, capitalist in its economy, libertarian in its laws and individualist in its society and pluralistic in its culture."  Fischer describes "Albion's Seed" as a modified Teutonic germ theory within the framework of the Frontier Thesis and the migration model.

Washington's Crossing (book): Washington's Crossing is a Pulitzer Prize-winning book written by David Hackett Fischer and part of the "Pivotal Moments in American History" series.  It is primarily about George Washington's leadership during the 1776 campaign of the American Revolutionary War, culminating with the famous crossing of the Delaware River and the subsequent campaign, with the Battle of Trenton, the Second Battle of Trenton, and the Battle of Princeton.

Furtive fallacy: The furtive fallacy is an informal fallacy of emphasis in which outcomes are asserted to have been caused by the hidden misconduct or wrongdoing by decision makers.  Historian David Hackett Fischer identified it as the belief that significant facts of history are necessarily sinister, and that "history itself is a story of causes mostly insidious and results mostly invidious."  It is more than a conspiracy theory in that it does not merely consider the possibility of hidden motives and deeds, but insists on them.  In its extreme form, the fallacy represents general paranoia.

David Souter: David Hackett Souter ( ; born September 17, 1939) is a retired Associate Justice of the Supreme Court of the United States.  He served from October 1990 until his retirement in June 2009.  Appointed by President George H. W. Bush to fill the seat vacated by William J. Brennan, Jr., Souter sat on both the Rehnquist and Roberts courts and came to vote reliably with the court's liberal members.

Champlain's Dream: Champlain’s Dream: The European Founding of North America is a biography written by American historian, David Hackett Fischer and published in 2008.  It is a biography of French "soldier, spy, master mariner, explorer, cartographer, artist and "Father of New France"", Samuel de Champlain.

Quakers in science: The Religious Society of Friends, commonly known as Quakers, encouraged some values which may have been conducive to encouraging scientific talents.  A theory suggested by David Hackett Fischer in his book "Albion's Seed" indicated early Quakers in the US preferred "practical study" to the more traditional studies of Greek or Latin popular with the elite.  Another theory suggests their avoidance of dogma or clergy gave them a greater flexibility in response to science.

Question: What story was written about Four British Folkways in America by David Hackett Fischer?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The name of the author who wrote the book."
    },
    "book_title": {
      "type": "string",
      "description": "The title of the book."
    },
    "book_subject": {
      "type": "string",
      "description": "A description of the book's primary subject matter."
    },
    "publication_year": {
      "type": "integer",
      "description": "The year the book was published."
    }
  },
  "required": [
    "author_name",
    "book_title",
    "book_subject",
    "publication_year"
  ],
  "additionalProperties": false
}
