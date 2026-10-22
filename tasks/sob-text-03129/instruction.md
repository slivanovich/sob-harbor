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
Lugus: Lugus was a deity of the Celtic pantheon.  His name is rarely directly attested in inscriptions, but his importance can be inferred from place names and ethnonyms, and his nature and attributes are deduced from the distinctive iconography of Gallo-Roman inscriptions to Mercury, who is widely believed to have been identified with Lugus, and from the quasi-mythological narratives involving his later cognates, Welsh Lleu Llaw Gyffes (Lleu of the Skillful Hand) and Irish Lugh Lámhfhada (Lugh of the Long Arm).

Fomorians: The Fomorians (Old Irish: Fomoire , Modern Irish: Fomhóraigh ) are a supernatural race in Irish mythology.  They are often portrayed as hostile and monstrous beings who come from the sea or underground.  Later, they were portrayed as giants and sea raiders.  They are enemies of Ireland's first settlers and opponents of the Tuatha Dé Danann, the other supernatural race in Irish mythology.  However, their relationship with the Tuath Dé is complex and some of their members intermarry and have children.  The Fomorians have thus been likened to the jötnar of Norse mythology.

Ler (mythology): Ler (meaning "Sea" in Old Irish; "Lir" is the genitive form) is a sea god in Irish mythology.  His name suggests that he is a personification of the sea, rather than a distinct deity.  He is named "Allód" in early genealogies, and corresponds to the Llŷr of Welsh mythology.  Ler is chiefly an ancestor figure, and is the father of the god Manannán mac Lir, who appears frequently in medieval Irish literature.  Ler appears as the titular king in the tale "The Children of Lir".

Emain Ablach: Emain Ablach (also Emne; Middle Irish Emhain Abhlach or Eamhna; meaning "Emhain of the Apples") is a mythical island paradise in Irish mythology.  It is often regarded as the realm of the sea god Manannán Mac Lir and identified with either the Isle of Man or the Isle of Arran.  According to the medieval Irish poem Baile Suthain Sith Eamhna, the god Lug Lamfada was reared in Emain Ablach.

Aos Sí: The aos sí (] , older form aes sídhe ] ) is the Irish term for a supernatural race in Irish mythology and Scottish mythology (usually spelled Sìth, however pronounced the same), comparable to the fairies or elves.  They are said to live underground in fairy mounds, across the western sea, or in an invisible world that coexists with the world of humans.  This world is described in the "Lebor Gabála Érenn" as a parallel universe in which the "aos sí" walk amongst the living.  In the Irish language, "aos sí" means "people of the mounds" (the mounds are known in Irish as "the "sídhe").  In Irish literature the people of the mounds are also called daoine sídhe ] ; in Scottish mythology they are daoine sìth.  They are variously said to be the ancestors, the spirits of nature, or goddesses and gods.

Goibniu: In Irish mythology Goibniu (Old Irish, pronounced ˈɡovʲnʲu ) or Gaibhne (Modern Irish) was the metalsmith of the Tuatha Dé Danann.  He is believed to have been a smithing god and is also associated with hospitality.

Mystic Knights of Tir Na Nog: Mystic Knights of Tir Na Nog is an Irish/American fantasy-adventure television series set in a fantasy version of ancient Ireland, created by Saban Entertainment.  It was loosely based on actual Irish mythology.  The name derives from Tír na nÓg, one of the Otherworlds of Irish mythology.  It was Saban's first fantasy series to involve knights, dragons, and wizards.  It aired on the Fox Kids block on Fox from September 1, 1998 and ending on May 7, 1999.  A second season entitled Mystic Knights: Battle Thunder was planned, but was later cancelled, and its budget was put towards "Power Rangers Lost Galaxy".  The resulting series was an attempt in doing an original non-Japanese special-effects series rather than adapting from actual Japanese tokusatsu.

Lugh: Lugh or Lug (] ; modern Irish: "Lú" ] ) is an important god of Irish mythology.  A member of the Tuatha Dé Danann, Lugh is portrayed as a youthful warrior hero, a king and saviour.  He is associated with skill, crafts and the arts as well as with oaths, truth and the law.  He is sometimes interpreted as a sun god, a storm god or a sky god.  Lugh is also strongly associated with the harvest festival of Lughnasadh, which is named after him.

Bébinn: Bébinn a.k.a. Bé Binn, is an early Irish name applied to a number of related and unrelated figures in Irish mythology.  In some sources Bébhinn (old orthography: Béḃinn) is a goddess associated with birth and the sister of the river-goddess, Boann.  Bébinn is also described as being an underworld goddess in both Irish and Welsh mythology, inhabiting either the Irish underworld Mag Mell or the Welsh Annwn, although it is unknown which is the original source.

Ogma: Ogma (modern spelling: Oghma) is a character from Irish mythology and Scottish mythology.  A member of the Tuatha Dé Danann, he is often considered a deity and may be related to the Gallic god Ogmios.

Question: The god of Irish mythology that is associated with Lugus is a member of what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "deity_name": {
      "type": "string",
      "description": "The name of the Irish god associated with Lugus."
    },
    "associated_group": {
      "type": "string",
      "description": "The group or pantheon the deity is a member of."
    },
    "reasoning_steps": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Steps taken to deduce the answer from the context."
    }
  },
  "required": [
    "deity_name",
    "associated_group",
    "reasoning_steps"
  ],
  "additionalProperties": false
}
