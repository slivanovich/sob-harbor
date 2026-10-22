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
The Battle of Maldon: The Battle of Maldon is the name given to an Old English poem of uncertain date celebrating the real Battle of Maldon of 991, at which the Anglo-Saxons failed to prevent a Viking invasion.  Only 325 lines of the poem are extant; both the beginning and the ending are lost.

Battle of Maldon: The Battle of Maldon took place on 10 or 11 August 991 CE near Maldon beside the River Blackwater in Essex, England, during the reign of Æthelred the Unready.  Earl Byrhtnoth and his thegns led the English against a Viking invasion.  The battle ended in an Anglo-Saxon defeat.  After the battle Archbishop Sigeric of Canterbury and the aldermen of the south-western provinces advised King Æthelred to buy off the Vikings rather than continue the armed struggle.  The result was a payment of 10,000 Roman pounds (3,300 kg) of silver, the first example of Danegeld in England.

Battle of Kretsch: The Battle of Kretsch occurred on 19 August 1435 and was the last real battle of the Hussite Wars.  A year earlier, the Battle of Lipany brought an end to most Hussite power in Bohemia, but some groups had still continued fighting.  Ulrich II von Rosenberg defeated the Taborites near the village of Kretsch, which brought an end to their ability to carry out attacks.  After this battle the radical Hussites at Tabor began to make an agreement with Emperor Sigismund.

Nad Niemnem (film): Nad Niemnem is a Polish historical film that follows the aftermath of the January Uprising.  It is about the lives of the families that lived on twenty years later.  Showing how the return to the classed society divided those families who once had fought as brothers.  This return to the old classed society resulted in a sense of betrayal on one side and guilty indignation on the other.  This until the niece of an estate owner befriends a neighboring family.  The neighbors who had lost their noble status still maintained a large tract of land which they farmed successfully themselves.  While her own uncle is on the verge of losing his estate because his brother in law is calling in an old loan of money.  The brother in law wants to spend the money on a big dowry and grand piano for his daughter.  The niece understands the financial position.  Her own father lost his estate and they both live with the uncle.  The niece finds more happiness in her new friendship with her neighbors than with those of her own class.  She begins to spend all her time next door learning to do the chores of a peasant farmer's wife.  This is unlike her aunt who spends her days reclining on a couch acting the grand lady.  The aunt is completely incapable of understanding how close she is to losing her couch.  From her couch the aunt entertains a wealthy suitor who is connected to the family.  But the niece declines the offer of marriage from this suitor.  The suitor is also a very sedate morphine addict but he is a noble.  Her family can not understand what she could be thinking to reject such an advantageous offer.  Until she marries the handsome peasant farmer next door.  The family grudgingly at first admit it is a very good match after all.  This alliance heals the breach between peasant and noble.  The old promises of solidarity between the neighbors are reaffirmed.  The ancestors resting in their graves overlooking the Niemnem are at peace.  Although they died fighting in the January Uprising the real battle was against the classed society.  A victory postponed and finally won,"Nad Niemnem" .

Battle of San Juan del Monte: The Battle of San Juan del Monte took place on 30 August 1896.  It is considered the first real battle of the Philippine Revolution, which sought Philippine independence from Spain.  The first battle cry of the Katipunan coincided with the pealing of the church bell at nine on the night of August 29, 1896.

Street Fighter: The Movie (console video game): Street Fighter: The Movie, released in Japan as Street Fighter: Real Battle on Film (ストリートファイター リアルバトル オン フィルム ) , is a head-to-head fighting game released for the PlayStation and Sega Saturn in 1995 .  The game is based on the 1994 live-action "Street Fighter" movie, itself based on the "Street Fighter" series of fighting games, and uses digitized images of the film' s cast as the characters.  While it shares its title with the arcade game "", the home version is not a port but a similar game developed on the same premise.  The home version was developed and published by Capcom in Japan and released in North America, Europe and Australia by Acclaim.

Byrhtnoth: Byrhtnoth was Ealdorman of Essex who died 11 August 991 at the Battle of Maldon.  His name is composed of the Old English "beorht" (bright) and "noth" (courage).  He is the subject of an ancient poem, and more recently a statue.

Tactical event: A tactical event (Also known as a "Private Battle" in the United Kingdom and elsewhere) is a type of historical reenactment, not usually open to the public, which is fought like a real battle with each side devising strategies and tactics to defeat their opponent(s).  Tactical events have no script, a basic set of agreed-upon rules (physical boundaries, time limit, victory conditions, etc.), and onsite judges or referees, and so could be considered a form of live action role-playing game.  Tactical battles might also be considered a form of experimental archaeology.

The Homecoming of Beorhtnoth Beorhthelm's Son: The Homecoming of Beorhtnoth Beorhthelm's Son is the title of a work by J. R. R. Tolkien that was originally published in 1953 in volume 6 of the scholarly journal "Essays and Studies by Members of the English Association", and later republished in 1966 in "The Tolkien Reader".  It is a work of historical fiction, inspired by the Old English poem "The Battle of Maldon".  It is written in the form of an alliterative poem, but is also a play, being mainly a dialogue between two characters in the aftermath of the Battle of Maldon.  The work was accompanied by two essays, also by Tolkien, one before and one after the main work.

Maeldune Centre: The Maeldune Centre is in Maldon, Essex in England.  It commemorates the Battle of Maldon.  Its address is Maeldune Centre, Plume Building, Market Hill, Maldon, Essex, England; phone: 01621-851628.  In it are the Millennium Embroidery, art displays, and Maldon Society photographic archives.  Its building was formerly St.Peter's Church, which had become redundant, as there are other churches in Maldon.

Question: when was  the work or j.rr inspried by the real battle of Maldon of 991 oriagnally pushled  

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "work_title": {
      "type": "string",
      "description": "The title of the work by J. R. R. Tolkien."
    },
    "author_name": {
      "type": "string",
      "description": "The name of the author of the work."
    },
    "inspired_by_event": {
      "type": "string",
      "description": "The historical event that inspired the work."
    },
    "original_publication_year": {
      "type": "integer",
      "description": "The year the work was originally published."
    },
    "publication_context": {
      "type": "string",
      "description": "Details about where the work was originally published."
    }
  },
  "required": [
    "work_title",
    "author_name",
    "inspired_by_event",
    "original_publication_year",
    "publication_context"
  ],
  "additionalProperties": false
}
