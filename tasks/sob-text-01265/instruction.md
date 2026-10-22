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
Big L: Lamont Coleman (May 30, 1974 – February 15, 1999), best known by his stage name Big L, was an American hip hop recording artist.  Coleman embarked on his career in rapping, with the hip hop trio, Three the Hard Way.  His first notable appearance came on Lord Finesse's "Yes You May (Remix)".  Coleman released his debut album, "Lifestylez ov da Poor & Dangerous", in 1995 and significantly contributed to the underground hip hop scene.  In 1998, he founded Flamboyant Entertainment, his own indie label, through which he released one of his most popular singles, "Ebonics" (1998).

ALIF (Liberate Attack of the Feminist Infantry): ALIF (Attaque libératoire de l'infanterie féministe, English: Liberation Attack of the Feminist Infantry) is the pioneer female hip hop trio of Hip Hop Galsen.  Emerging in the late mid-1990s, ALIF offered a feminine and feminist flavour to Hip Hop Galsen encouraging women to play their part in the movement.  The group split beginning of 2010 after thirteen years of a memorable career.

Illuminati X: Illuminati X (AKA!!  Street Team Balkan Beasts!!!)  is a Serbian-Canadian hip hop trio composed of rappers Luxie and Lochie Max and Kreemie Yung.  The group's members were all born in the former Yugoslavia, and emigrated to Canada in the mid-90's after the outbreak of civil war.  They gained a little buzz locally in Niagara Falls while still in their teens due to family connections and style of hip hop amongst local serbians, which involved combining hip hop beats with serbian folk samples and nationalistic lyrics.  Today, the group's music is mostly sample-free.  They rap mostly in the English language.  These 3 young balkan rappers are simply legendary.  Their creative beats go along with their wicked lyrics and make an amazing combo.

De La Soul: De La Soul is an American hip hop trio formed in 1987 on Long Island, New York.  The group is best known for their eclectic sampling, quirky lyrics, and their contributions to the evolution of the jazz rap and alternative hip hop subgenres.  The members are Posdnuos, Dave and Maseo.  The three formed the group in high school and caught the attention of producer Prince Paul with a demo tape of the song "Plug Tunin'".  With its playful wordplay, innovative sampling, and witty skits, the band's debut album, "3 Feet High and Rising", has been called "a hip hop masterpiece."

Warp 9: Warp 9, a science fiction themed electro-funk and hip hop trio, best known for their influential singles "Nunk," "Light Years Away," and "Beat Wave," ranks among the most iconic groups of the electro hip hop era.  Described as the "perfect instance of hip hop's contemporary ramifications," Warp 9 was the brainchild of writer-producers Lotti Golden and Richard Scher.  The duo wrote and recorded under the moniker Warp 9, a production project at the forefront of the electro movement.  Warp 9 evolved from a studio concept into a band when Prism Records expressed interest in releasing Nunk as a single.  Golden & Scher invited drummer Chuck Wansley and percussionist Boe Brown to perform the male vocals and rhymes.  Later, a female vocalist was added to the group; Ada Dyre performed vocals and rhymes for Warp 9's second single, "Light Years Away."  The group released two albums, "It's a Beat Wave" (1983), (Island Records), a street themed testament exploring the topics of science fiction, hip hop and mixing, and "Fade In, Fade Out" (Motown), (1986), a soul R&B oriented montage.  Warp 9's image is best described on the cover of their 12" single "Light Years Away," with Milton (Boe) Brown (Warp 9's lead singer), Chuck Wansley and session singer Ada Dyer in their trademark sci-fi space suits.

The Cactus Album: The Cactus Al/Bum (also known as The Cactus Cee/D and The Cactus Cas/Ette depending on release format) is the debut album by hip hop trio 3rd Bass, released on Def Jam Recordings on November 14, 1989.  The album received positive reviews from the hip hop press, and the group gained some publicity by being arguably the second white group to achieve hip hop credibility, after the Beastie Boys.  It was certified gold by the RIAA on April 24, 1990, the same day as Biz Markie's "The Biz Never Sleeps", which was released two weeks prior to "The Cactus Album".

McGruff (rapper): Herbert Brown, better known by his stage name McGruff (also known as Herb McGruff) is an American Hip hop recording artist from Harlem, New York City, New York.  Brown started rapping in his early teens.  He embarked on his music career in the hip hop group Bronx Most Wanted, alongside rappers Jay Q and Tee U.B. Brown later became a member of the hip hop collective Children of the Corn.  As a member of Children of the Corn, Brown worked alongside Big L, Cam'ron, Bloodshed and Mase, all of whom would go on to have successful careers in the music industry.  After the group disbanded without releasing any material, Brown made his first appearance on Big L's debut album, "Lifestylez ov da Poor & Dangerous" (1995), on the tracks "8 Iz Enuff" and "Dangerzone".  Eventually, Brown signed a deal with popular hip hop label, Uptown Records and began recording his debut album, "Destined to Be".  In early 1998, the album's lead single "Before We Start" became a minor hit, charting on several "Billboard" charts.  In the Summer of 1998, "Destined to Be" was released but failed to sell many copies, only peaking at 169 on the "Billboard" 200, and Brown was released from his contract.  Brown would make appearances with Heavy D on his album, "Waterbed Hev" and the "Woo" soundtrack.  In 2009, Brown appeared on Mase's mixtape "I Do the Impossible".  In 2010, he was featured heavily on The Diplomats mixtape, "The D.I.P. Agenda."  In 2014, DJ Kay Slay, enlisted Brown, along with Raekwon, Fat Joe, Ghostface Killah, Sheek Louch, N.O.R.E., Lil' Fame, Prodigy and Rell, for a song titled "90s Flow".

Are You In?: Nike+ Original Run: Are You In? : Nike+ Original Run (a pun on "R-U-N") is an iTunes exclusive mixtape by hip hop trio De La Soul, in association with Nike.  The album is produced by Flosstradamus.  In the past, De La Soul collaborated with Nike to make designer shoes, and months later was picked to be a part of Nike's "Original Run" series, aimed at runners.  "Are You In?"  was the first album by De La Soul in five years and is one long continuous mixtape released on iTunes with an additional digital booklet.  It was generally well received by music and hip hop critics and was reviewed by "Wired", "Urb", and the "Hip Hop DX" online magazine.

The Hard Way (213 album): The Hard Way is the only studio album from American hip hop trio 213, which consisted of Snoop Dogg, Warren G and Nate Dogg.  The reunion of the group first appeared as 213 in Warren G's "The Return of the Regulator" in the track "Yo' Sassy Ways".  In 2003, Snoop Dogg, released his series of mixtapes, from which the second compilation "Welcome to tha chuuch, Vol.  2" included the first version of "So Fly", which is a parody of the then chart-running hit single by Monica, So Gone.  Missy Elliott, a co-producer of the song (with Spike & Jamahl), got to hear the tape and was very impressed by it.  She agreed with Snoop to cede the right of the sample for the upcoming 213 project in exchange for their rapping on Tamia's "Can't Go for That" remix.  In the end it came out to be the first unofficial radio single of "The Hard Way" and was performed live at BET's 106 & Park.  The album version differs from the mixtape version in a way that it is five seconds shorter and misses Snoop's intro where he gives the shootouts "Welcome to tha chuuch Vol.  2...exclusive 213".  The official debut retail single was "Groupie Luv", which was also accompanied by a promo video.  It was directed by Chris Robinson and was filmed in Snoop Dogg's own house (see also Still a G Thang).  It is also the video debut for dancer Criscilla Crossland.

The Score (Fugees album): The Score is the second and final studio album by the hip hop trio Fugees, released worldwide February 13, 1996 on Columbia Records.  The album features a wide range of samples and instrumentation, with many aspects of alternative hip hop that would come to dominate the hip hop music scene in the mid-late 1990s.  "The Score"'s production was handled mostly by the Fugees themselves and Jerry Duplessis, with additional production from Salaam Remi, John Forté, Diamond D, and Shawn King.  The album's guest raps are from Outsidaz members Rah Digga, Young Zee and Pacewon, as well as Omega, John Forté, and Diamond D. Most versions of the album feature four bonus tracks, including three remixes of "Fu-Gee-La", and a short acoustic Wyclef Jean solo track entitled "Mista Mista".

Question: Who has McGruff works alongside who started with the hip hop trio, Three the Hard Way?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "collaborator_name": {
      "type": "string",
      "description": "The name of the artist who worked alongside McGruff."
    },
    "started_with_trio": {
      "type": "boolean",
      "description": "Indicates if the collaborator started their career with the hip hop trio 'Three the Hard Way'."
    },
    "trio_name": {
      "type": "string",
      "description": "The name of the hip hop trio the collaborator started with."
    }
  },
  "required": [
    "collaborator_name",
    "started_with_trio",
    "trio_name"
  ],
  "additionalProperties": false
}
