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
Notes from San Francisco: Notes from San Francisco is a posthumous album by Irish musician Rory Gallagher.  Released in 2011, It consists of two CDs.  The first disc is a never released album that Gallagher recorded in San Francisco in December 1977.  The album was to be a major shift for Gallagher.  Rather than producing it himself he worked with Elliot Mazer a successful producer who had a long track record with artists such as Bob Dylan, Janis Joplin, and The Band.  At the last minute -- causing great distress to his manager and brother Donal and to his record company -- Gallagher decided to just pull the record.  In an interview Gallagher stated "it wasn't because of the material or the musicians or anything like that.  It was a song thing that I didn't think on the technical side everything worked.  So I scrapped the thing" After scrapping the album Gallagher reworked his band firing all the musicians except the bass player and hiring a new drummer.  This new Gallagher power trio re-recorded the San Francisco songs with Gallagher producing and released them as Photo-Finish.  Shortly before his death, Rory reportedly gave Donal permission to eventually release the original San Francisco versions of the songs if they were remixed.  Donal had his son Daniel remix the songs in 2011.  The second disc is a live performance also recorded in San Francisco in December 1979.

San Francisco Seals (soccer): San Francisco Seals began as the senior team of the San Francisco United Soccer Club founded in 1985, a 501c3.  The club is based in San Francisco, California.  In 1992, the SFUSC youth team started playing as the "All Blacks" in the top tier of the USISL when Cal North Soccer, the governing body of youth soccer closed the youth program by blocking the movement of players across boundaries.  The team played its home games at Negoesco Stadium on the campus of the University of San Francisco.  The team's colors were black, red and white.  After the first season and for five straight seasons the Seals dominated soccer on the West Coast winning 5 division titles, 3 regional titles and went to 3 national championship finals.  In 1997 the Seals was called the "Team of the Year" by USA today after beating the Seattle Sounders, the Kansas City Wiz (now Sporting), and the San Jose Clash (now Earthquakes) in the Lamar Hunt U.S. Open Cup.  The Seals continued in the A-League until 2000 when the franchise stopped professional soccer and returned to youth development.  The Seals continued as members of the Y-League and expanded their youth development to include college level players in 2006 by entering the PDL.  Since 2009 the Seals have concentrated on youth development from U6 to U23 soccer.

The Tenderloin Times: The Tenderloin Times was a free monthly newspaper serving the Tenderloin district of San Francisco, published from the 1970s to the 1990s, with a circulation of 15,000.  Its pages were filled with news on homelessness, social programs affecting the area's residents, immigration, neighborhood history and other topics.  Its investigative reports on issues such as the death of homeless people on San Francisco streets and the high rate of pedestrians hit by cars in the neighborhood were often picked up by mainstream media.  One page was devoted to poetry written by Tenderloin residents and participants in a weekly writing workshop held at Hospitality House in the neighborhood.  The writing in the paper was praised by Pulitzer Prize–winning columnist Herb Caen of the "San Francisco Chronicle", and was profiled positively in the New York Times, the Los Angeles Times, the San Francisco Examiner and Columbia Journalism Review.  Starting in 1985, the paper was published in four languages: English, Lao, Khmer and Vietnamese - reflecting the ethnic diversity of the neighborhood's residents.  Rob Waters, later a freelance journalist and a reporter for Bloomberg News, and Sara Colm, now a senior researcher at Human Rights Watch, worked as editors.

San Francisco Chronicle Magazine: The San Francisco Chronicle Magazine is a Sunday magazine published on the first Sunday of every month as an insert in the "San Francisco Chronicle".  The current magazine was born out of the ashes of "The San Francisco Examiner Magazine" when the staff of the "Chronicle" and "The San Francisco Examiner" were combined in 2000 following the sale of the "Examiner".

InformationWeek: InformationWeek is a digital magazine which conducts corresponding face-to-face events, virtual events, and research.  It is headquartered in San Francisco, California and was first published in 1985 by CMP Media, later called CMP Technology.

Simon Sheppard (writer): Simon Sheppard is a writer of gay erotica and a sex-advice columnist from San Francisco.  He is the author of many books of gay sex writing, including "Man on Man: The Best of Simon Sheppard", "Sodomy!" , "Jockboys," "Kinkorama: Dispatches From the Front Lines of Perversion," "In Deep", and "Sex Parties 101".  He is also the editor of "Homosex: 60 Years of Gay Erotica," winner of the 2007 Lambda Literary Award for LGBT erotica; the anthology "Leathermen"; and is the coeditor of the anthologies "Rough Stuff" and "Roughed Up."  Sheppard's work is wide-ranging, often combining history, philosophy, and culture — high and low — with hardcore sex.  His first book, "Hotter Than Hell and Other Stories", won the Erotic Authors Association Award for Best Collection of the Year, and the title story of "In Deep" was shortlisted for the Rauxa Prize for Erotic Fiction.  His work has also appeared in over 300 anthologies and magazines, including many editions of "Best Gay Erotica" and "The Best American Erotica".  He wrote the syndicated column "Sex Talk," and the online columns "Perv" and "Notes of a Cranky Old Fag."  The online serial "The Dirty Boys' Club,” which he wrote for OutPersonals, was published as a novel in 2012.  He also curates and co-hosts, with Carol Queen, the San Francisco performance series Perverts Put Out!  Sheppard is openly gay, and is active in the queer artistic, political and AIDS-activist communities.  He lives with his husband in San Francisco, where "San Francisco" magazine dubbed him “our erotica king.”

Cyrus Saatsaz: Cyrus Saatsaz is a journalism professor at the University of Houston and was formerly an instructor in the Journalism & Media Studies department at San Diego State University, the host of WaXed a surf talk show radio show that aired on ESPN 1700 in Southern California, is the author of "Dogwild & Board: Stories, Interviews and Musings from a Surf Journalist", and is a writer for The Huffington Post and GrindTV.com which is associated with Yahoo Sports.  Saatsaz was an editor with USA Today for nine years.  Saatsaz hosted and was Editor-in-Chief of The Extreme Scene, the world's first action sports radio talk show.  In addition to writing for The Huffington Post, Saatsaz is an award winning journalist, having been published in newspapers, magazines, books and websites including the San Francisco Chronicle and its official website SFGate. com, USA Today, AOL.com, Future Snowboarding Magazine, Fuel.TV, The Great Book of San Francisco/Bay Area Sports Lists, and many more.  Saatsaz is the founder of a surf shop/bookstore/art gallery in San Francisco called San Francisco Surf Company.  Saatsaz also worked for KNBR 680/1050 in San Francisco and The Mighty 1090 and ESPN 1700 in San Diego for 14 years, serving as a sports anchor, host, Creative Director and Executive Producer.

Nisekoi: Nisekoi (ニセコイ , lit.  "Fake Love") , released in English as Nisekoi: False Love, is a Japanese romantic comedy manga series written and illustrated by Naoshi Komi.  "Nisekoi" was first published as a one-shot manga in Shueisha's seasonal "Jump NEXT! " magazine before being serialized in "Weekly Shōnen Jump".  Since November 26, 2012, "Nisekoi" has been published in English in Viz Media's digital magazine, "Weekly Shonen Jump".  As of October 2016, the series has been compiled in 25 "tankōbon" volumes in Japan, and is also being released in English in digital and print volumes by Viz Media.  The manga has inspired a novel series, titled "Nisekoi: Urabana", written by Hajime Tanaka and published by Shueisha.  There have been two volumes published, on June 4 and December 28, 2013.

David M. Ewalt: David M. Ewalt (born 1976) is an American journalist.  He is currently deputy editor of special projects at Forbes.  Prior to joining "Forbes" he worked at "Newsday", "InformationWeek" and "The Stony Brook Press".

Theodore Wores: Theodore Wores (August 1, 1859–September 11, 1939) was an American painter born in San Francisco, son of Joseph Wores and Gertrude Liebke.  His father worked as a hat manufacturer in San Francisco.  Wores began his art training at age twelve in the studio of Joseph Harrington, who taught him color, composition, drawing and perspective.  When the San Francisco School of Design opened in 1874, Wores was one of the first pupils to enroll.  After one year at that school under the landscape painter Virgil Macey Williams, he continued his art education at the Royal Academy in Munich where he spent six years.  He also painted with William Merritt Chase and Frank Duveneck.  Wores returned to San Francisco in 1881.  He went to Japan for two extended visits and had successful exhibitions of his Japanese paintings in New York City and London, where he became friends with James Abbott McNeill Whistler and Oscar Wilde.  He visited Hawaii and Samoa in 1901-1902 and established a home in San Francisco about 1906.  He visited Hawaii for a second time in 1910–1911.  He was married in 1910 in San Francisco to Carolyn Bauer.  For the remainder of his career, Wores painted the coast on the western edge of San Francisco.  He died from a heart attack in San Francisco Sept. 11, 1939.

Question: David M. Ewalt worked at a digital magazine which is headquartered in San Francisco, and was first published in 1985 by who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine_name": {
      "type": "string",
      "description": "The name of the digital magazine."
    },
    "publisher": {
      "type": "string",
      "description": "The company that first published the magazine."
    },
    "headquarters_city": {
      "type": "string",
      "description": "The city where the magazine is headquartered."
    },
    "first_published_year": {
      "type": "integer",
      "description": "The year the magazine was first published."
    },
    "employee_name": {
      "type": "string",
      "description": "The name of the individual who worked at the magazine."
    }
  },
  "required": [
    "magazine_name",
    "publisher",
    "headquarters_city",
    "first_published_year",
    "employee_name"
  ],
  "additionalProperties": false
}
