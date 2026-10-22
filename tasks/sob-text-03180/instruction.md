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
The Iron Maidens: The Iron Maidens is an American heavy metal band from Los Angeles, California.  Formed in 2001 as an all-female tribute act to English heavy metal band Iron Maiden.  Considered the "World's Only Female Tribute to Iron Maiden," the band currently consists of vocalist Kirsten Rosenberg, bassist Wanda Ortiz, drummer Linda McDonald, guitarist Courtney Cox, and guitarist Nikki Stringfield,

Venom (band): Venom are an English heavy metal band formed in 1979 in Newcastle upon Tyne.  Coming to prominence towards the end of the new wave of British heavy metal, Venom's first two albums—"Welcome to Hell" (1981) and "Black Metal" (1982)—are considered a major influence on thrash metal and extreme metal in general.  Venom's second album proved influential enough that its title was used as the name of an extreme metal subgenre: black metal.

Shoot Out the Lights (song): "Shoot Out the Lights" is a single by heavy metal band Diamond Head released in 1980 by Happy Face Records, the band's own label.  It was a single A-side with "Shoot Out the Lights" and "Helpless" as the B-side, and was only available on 7", without a picture sleeve in order to reduce production costs.  The latter song was covered by thrash metal band Metallica on their 1987 "$5.98 EP: Garage Days Re-revisited" EP.  An extended version of "Helpless" appeared on Diamond Head's 1980 debut Lightning to the Nations, and "Shoot Out the Lights" eventually appeared on an expanded version of the debut album released in 2001 by Sanctuary Records.  The EP received much criticism from heavy metal fans claiming that "it wasn't metal enough."  The band, though scoffing at these comments, was seen in live concerts playing more hardcore versions of beloved songs.

Jesters of Destiny: Jesters of Destiny is a heavy metal band from Los Angeles, California, which was formed in 1984 by Bruce Duff (bass/vocals, who had been booted from 45 Grave earlier in the year) and guitarist Ray Violet.  Evolving from a recording project spearheaded by Violet, who was working as the house engineer for Dawnbreaker studio in San Fernando, CA (previously owned by Seals and Crofts), the band recorded what would be the first two Jesters songs during the project,which was instigated in order to come up with commercial jingles.  The songs were "Diggin' That Grave" and "End of Time."  The band presented the songs to Metal Blade Records, who included "End of Time" on Metal Massacre V collection.  It closed the LP, which include early tracks by Overkill, Fates Warning, Voi Vod and Metal Church.  The band then signed to Metal Blade, but due to the band not being strictly heavy metal, the label created a subsidiary, Dimension Records, which released the band's debut album, "Fun at the Funeral", in 1986, and an EP, "In a Nostalgic Mood", in 1987, during their first tenure.  Following ",,"Mood,"" Metal Blade dropped the band.  They demo-ed a number of songs for a planned third LP to be titled, "No Laughing Matter," but we're unable to land a new recording contract.  They broke up in 1988.  During their run, a number of lead guitarists and drummers were part of the band, including on drums, David Buzzelli (Doktor Stixx), Louie Schilling, Walin' Jennings Morgan, Dave Kuzma, Blaze; and on guitar, Sickie Wifebeater, Michael Montano and Brian Butler.

The End Tour: The End Tour was the farewell tour of the heavy metal band Black Sabbath, featuring founding members Ozzy Osbourne, Tony Iommi and Geezer Butler.  The tour concluded Sabbath's 40+ year career.  The final show was February 4, 2017, in their home city of Birmingham, UK.

Saxon (band): Saxon are an English heavy metal band formed in 1977, in South Yorkshire.  As one of the leaders of the new wave of British heavy metal, they had eight UK Top 40 albums in the 1980s including four UK Top 10 albums and two Top 5 albums.  The band also had numerous singles in the UK Singles Chart and chart success all over Europe and Japan, as well as success in the US.  During the 1980s Saxon established themselves as one of Europe's biggest metal acts.  The band tours regularly and have sold more than 15 million albums worldwide.  They are considered one of the classic metal acts and have influenced many bands such as Metallica, Mötley Crüe, Pantera, Sodom.

Welcome to Hell: Welcome to Hell is the debut studio album by English heavy metal band Venom.  It was released in December 1981, through Neat Records, at the culmination of the new wave of British heavy metal movement.  The music of "Welcome to Hell" is often described as speed metal, but it had a great influence on the then-emerging thrash metal style, and crystallised the elements of what later became known as death metal and black metal.

Black Metal (Venom album): Black Metal is the second album by English heavy metal band Venom.  It was released in November 1982, during the great flourishing of metal music in the UK that was the new wave of British heavy metal, and is considered a major influence on the thrash metal, death metal and black metal scenes that emerged in the 1980s and early 1990s.

No Prayer for the Dying: No Prayer for the Dying is the eighth studio album by English heavy metal band Iron Maiden.  It marks their first line-up change since 1982; guitarist Adrian Smith left the band during the pre-production phase, unhappy with the musical direction it was taking, and only having contributed to one song, "Hooks in You".  Smith was replaced by Janick Gers, who had previously worked with singer Bruce Dickinson on his first solo-album, "Tattooed Millionaire", and had also worked with Ian Gillan, former Marillion singer Fish, and new wave of British heavy metal band, White Spirit.

The End (EP): The End is an EP by English heavy metal band Black Sabbath, released on January 20, 2016.  It was only available at dates on their final tour The End.  The EP's first four tracks are unreleased songs from the "13" sessions, and the rest were recorded live on that album's tour in 2013–2014.

Question:  The End is an EP by an English heavy metal band which was only available at dates with the  final show was February 4, 2017, in their home city of what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the heavy metal band."
    },
    "ep_details": {
      "type": "object",
      "properties": {
        "ep_name": {
          "type": "string",
          "description": "The name of the EP."
        },
        "release_date": {
          "type": "string",
          "description": "The release date of the EP."
        },
        "availability_condition": {
          "type": "string",
          "description": "The condition under which the EP was available."
        }
      },
      "required": [
        "ep_name",
        "release_date",
        "availability_condition"
      ],
      "additionalProperties": false
    },
    "final_tour_details": {
      "type": "object",
      "properties": {
        "tour_name": {
          "type": "string",
          "description": "The name of the farewell tour."
        },
        "final_show_date": {
          "type": "string",
          "description": "The date of the final show."
        },
        "final_show_location": {
          "type": "object",
          "properties": {
            "city": {
              "type": "string",
              "description": "The city where the final show took place."
            },
            "country": {
              "type": "string",
              "description": "The country where the final show took place."
            }
          },
          "required": [
            "city",
            "country"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "tour_name",
        "final_show_date",
        "final_show_location"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "band_name",
    "ep_details",
    "final_tour_details"
  ],
  "additionalProperties": false
}
