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
Silent Night, Deadly Night: Silent Night, Deadly Night is a 1984 American slasher film directed by Charles E. Sellier, Jr., and starring Robert Brian Wilson, Lilyan Chauvin, Gilmer McCormick, Toni Nero, Linnea Quigley, Britt Leach and Leo Geter.  Set during Christmas, the story concerns a young man, Billy, who suffers from posttraumatic stress over witnessing his parents' Christmas Eve murder and his subsequent upbringing in an abusive Catholic orphanage.  In adulthood, the Christmas holiday leads him into a psychological breakdown, and he emerges as a spree killer donning a Santa suit.

Harper's Weekly: Harper's Weekly, A Journal of Civilization was an American political magazine based in New York City.  Published by Harper & Brothers from 1857 until 1916, it featured foreign and domestic news, fiction, essays on many subjects, and humor, alongside illustrations.  It carried extensive coverage of the American Civil War, including many illustrations of events from the war.  During its most influential period, it was the forum of the political cartoonist Thomas Nast.

Santa suit: A Santa suit is a costume worn by a person portraying Santa Claus.  The modern American version of the suit can be attributed to the work of Thomas Nast for "Harper's Weekly" magazine, although it is often incorrectly thought that Haddon Sundblom designed the suit in his advertising work for the Coca-Cola Company.  Sundblom's work did standardize the western image of Santa, and popularized the image of the red suit with white fur trim.  This has become the image of the American Santa, while in some European countries where Saint Nicholas remains popular, the outfit worn is closer to religious clothing, including a Bishop's mitre.

The Gilded Age: A Tale of Today: The Gilded Age: A Tale of Today is a novel by Mark Twain and Charles Dudley Warner first published in 1873.  It satirizes greed and political corruption in post–Civil War America in the era now referred to as the Gilded Age.  Although not one of Twain's best-known works, it has appeared in more than one hundred editions since its original publication.  Twain and Warner originally had planned to issue the novel with illustrations by Thomas Nast.  The book is remarkable for two reasons–-it is the only novel Twain wrote with a collaborator, and its title very quickly became synonymous with graft, materialism, and corruption in public life.

Covina massacre: The Covina massacre occurred on December 24, 2008, in Covina, a city in the suburbs of Los Angeles, California, United States.  Nine people were killed, either by gunshot wounds or in an arson fire inside a house on 1129 East Knollcrest Drive, where a Christmas Eve party was being held.  The perpetrator, 45-year-old Bruce Jeffrey Pardo, who entered the house wearing a Santa suit, committed suicide, dying from a gunshot wound to the head at his brother's residence in the early morning hours after the attack.  Authorities cited marital problems as a possible motive for the violence; reports indicated that Pardo's divorce had been finalized on December 18, one week before the massacre.  Three people, including Pardo's ex-wife and his former in-laws, were initially declared missing pending identification of their bodies.

Thomas Nast Home: The Thomas Nast Home, also known as Villa Fontana, was the home of German born Thomas Nast in Morristown, Morris County, New Jersey, United States.  He was a editorial cartoonist whose drawings in "Harpers Weekly" contributed to the downfall of Tammany Hall.  He is also known as the creator of several iconic images such as Santa Claus, the Democratic Donkey, and the Republican Elephant.

Christmas in the American Civil War: Christmas in the American Civil War (1861–1865) was celebrated in both the United States and the Confederate States of America although the day did not become an official holiday until five years after the war ended.  The war continued to rage on Christmas and skirmishes occurred throughout the countryside.  Celebrations for both troops and civilians saw significant alteration.  Propagandists, such as Thomas Nast, used wartime Christmases to reflect their beliefs.  In 1870, Christmas became an official Federal holiday when President Ulysses S. Grant made it so in an attempt to unite north and south.

Santa Claus in film: Motion pictures featuring Santa Claus abound and apparently constitute their own subgenre of the Christmas film genre.  Early films of Santa revolve around similar simple plots of Santa's Christmas Eve visit to children.  In 1897, in a short film called "Santa Claus Filling Stockings", Santa Claus is simply filling stockings from his pack of toys.  Another film called "Santa Claus and the Children" was made in 1898.  A year later, a film directed by George Albert Smith in titled "Santa Claus" (or "The Visit from Santa Claus" in the United Kingdom) was created.  In this picture, Santa Claus enters the room from the fireplace and proceeds to trim the tree.  He then fills the stockings that were previously hung on the mantle by the children.  After walking backward and surveying his work, he suddenly darts at the fireplace and disappears up the chimney.  "Santa Claus' Visit" in 1900 featured a scene with two little children kneeling at the feet of their mother and saying their prayers.  The mother tucks the children snugly in bed and leaves the room.  Santa Claus suddenly appears on the roof, just outside the children's bedroom window, and proceeds to enter the chimney, taking with him his bag of presents and a little hand sled for one of the children.  He goes down the chimney and suddenly appears in the children's room through the fireplace.  He distributes the presents and mysteriously causes the appearance of a Christmas tree laden with gifts.  The scene closes with the children waking up and running to the fireplace just too late to catch him by the legs.  A 1909 film by D. W. Griffith titled "A Trap for Santa Claus" shows children setting a trap to capture Santa Claus as he descends the chimney, but instead capture their father who abandoned them and their mother but tries to burglarize the house after he discovers she inherited a fortune.  A twenty-nine-minute 1925 silent film production titled "Santa Claus", by explorer/documentarian Frank E. Kleinschmidt, filmed partly in northern Alaska, feature Santa in his workshop, visiting his Eskimo neighbors, and tending his reindeer.  A year later, another movie titled "Santa Claus" was produced with sound on De Forest Phonofilm.  Over the years, various actors have donned the red suit (aside from those discussed below), including Monty Woolley in "Life Begins at Eight-thirty" (1942), Alberto Rabagliati in "The Christmas That Almost Wasn't" (1966), Dan Aykroyd in "Trading Places" (1983), Jan Rubes in "One Magic Christmas" (1985), David Huddleston in "" (1985), Jonathan Taylor Thomas in "I'll Be Home for Christmas" (1998), and Ed Asner in "Elf" (2003).  Later films about Santa vary, but can be divided into the following themes.

Thomas Nast: Thomas Nast ( ; ] ; September 27, 1840 – December 7, 1902) was a German-born American caricaturist and editorial cartoonist considered to be the "Father of the American Cartoon".  He was the scourge of Democratic Representative "Boss" Tweed and the Tammany Hall Democratic party political machine.  Among his notable works were the creation of the modern version of Santa Claus (based on the traditional German figures of Sankt Nikolaus and Weihnachtsmann) and the political symbol of the elephant for the Republican Party (GOP).  Contrary to popular belief, Nast did not create Uncle Sam (the male personification of the American people), Columbia (the female personification of American values), or the Democratic donkey, though he did popularize these symbols through his artwork.  Nast was associated with the magazine "Harper's Weekly" from 1859 to 1860 and from 1862 until 1886.

Ferdinand Ward: Ferdinand De Wilton Ward, Jr. (1851–1925), known first as the "Young Napoleon of Finance," and subsequently as "the Best-Hated Man in the United States," was an American swindler.  Ward caused the financial ruin of many people, including many famous people such as Thomas Nast and the former U.S. President Ulysses S. Grant, who had helped him start his banking business.

Question: Today's American image of the Santa suit, created by Thomas Nast, is based off of which traditional German figures?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "creator_name": {
      "type": "string",
      "description": "The name of the person credited with creating the modern American image."
    },
    "creation_description": {
      "type": "string",
      "description": "A description of what was created or popularized."
    },
    "source_figures": {
      "type": "array",
      "description": "A list of traditional figures or concepts that the creation was based upon.",
      "items": {
        "type": "string"
      }
    },
    "source_country": {
      "type": "string",
      "description": "The country of origin for the source figures."
    }
  },
  "required": [
    "creator_name",
    "creation_description",
    "source_figures",
    "source_country"
  ],
  "additionalProperties": false
}
