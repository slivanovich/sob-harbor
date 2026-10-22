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
Devi-Bhagavata Purana: The Devi Bhagavata Purana (Sanskrit: देवी भागवतपुराण, "Devī Bhāgavatapurāṇa "), also known as the Shrimad Devi Bhagvatam and the Devi Bhagavatam, is a Sanskrit text that belongs to the Purana-genre of Hindu literature.  The text is considered a "Mahapurana" (major Purana) in parts of India, while others include it as one of the "Upapurana" (minor Purana), but all traditions consider it as an important Purana.

Adi Parashakti: According to Shaktism and Hindu mythology, Adi Para Shakti—the Goddess, Devi—is the Supreme Being.  She is also popularly referred to as "Adi Shakti", "Parama Shakti", "Maha Shakti", "Mahadevi", or even simply as "Shakti".  "Parama" means "absolute", "Satya" means the Truth as per many Shakta texts.  The Devi Bhagavata Mahapurana states that Adi Parashakti is the original creator, observer and destroyer of the whole universe.

Parashakthi Temple: Parashakthi Temple, also known as Eternal Mother Temple is a tirtha peetham (pilgrimage) in the west for Devi Adi Parashakti Durga worshipers situated in the heart of Pontiac, Michigan, United States.  The Temple was built in 1999 and the inaugural pooja took place on Vijayadasami day.  The Temple land is known for its mystical properties and was once home to the powerful Native American healers.

Mahavishnu: Mahavishnu (Devanāgarī : महाविष्णु) is an aspect of Vishnu, the Absolute which is beyond human comprehension and is beyond all attributes.  In Gauḍīya Vaishnavism, a school of Vaiṣṇavism, the Sātvata-tantra describes three different forms, or aspects, of Vishnu as Mahavishnu, Garbhodakśayī-Viṣṇu and Kṣīrodakaśāyī Vishnu.  The term Mahavishnu is similar to Brahman and Almighty Absolute Supreme Personality of Godhead.  This means that the Absolute truth is realized first as Brahman (impersonal aspect) then as Paramatma (personal aspect) and finally as Bhagavan (incarnate perfection).  So bhakti (loving devotion) goes to Bhagavan, Krishna or Rama for instance (avatars or incarnations of Vishnu, Narayana).  In this way, bhakti surpasses even yoga, which is aimed at the Supersoul, Paramatma.  Mahavishnu is the Supersoul of all living beings (jivaatmas) in all material universes.  It is also often used interchangeably with Vishnu to indicate reverence, as the prefix "Mahā" exalts the noun to which it is attached.  It is believed that Adi Parashakti has been created by Maha Vishnu to maintain the Material Universe.  So Parashakti is working under the direction of Maha vishnu.  So all the Gods including Shiva, Parashakti, Brahma are considered as the Part of Maha Vishnu Expansion. [citation needed]

Kali: Kālī ( ; Sanskrit: काली ), also known as Kālikā (Sanskrit: कालिका ), is a Hindu goddess.  Kali's earliest appearance is that of a destroyer of evil forces.  She is the goddess of one of the four subcategories of the Kulamārga, a category of tantric Saivism.  Over time, she has been worshipped by devotional movements and tantric sects variously as the Divine Mother, Mother of the Universe, Adi Shakti, or Adi Parashakti.  Some Shakta Hindu and Tantric sects, particularly ones who follow the Kalikula system, additionally worship her as the ultimate reality or "Brahman".  She is also seen as divine protector and the one who bestows "moksha", or liberation.  Kali is often portrayed standing or dancing on her consort, the Hindu god Shiva, who lies calm and prostrate beneath her.  Kali is worshipped by Hindus throughout India.  Kali is one of the ten Mahavidyas, a list which combines Sakta and Buddhist goddesses.

Shaktheeswaram Temple: Shaktheeswaram Temple is a Hindu temple located in Kottayam, India.  The main deity of the temple is Goddess Adi Parashakti.  Adi Parashakti is the female aspect of the divine venerated as the Supreme Being in Shaktism.  The temple is also a center where Traditional Astrology, Tantric Upasana, Sanathana Dharma and the most auspicious pooja in Hinduism called Sri Chakra Pooja is practiced by Head Priest and Tantracharya Sri Kasi Viswanathan.

Chandi: Chandi (Sanskrit: Caṇḍī ) or Chandika (Caṇḍīka ) is a Hindu goddess.  Chandi is the combined form of Lakshmi, Saraswati and Durga, the ferocious form of Parvati.  She is said to be the most ferocious incarnation of Adi Parashakti.  Chandika form is said to be extremely ferocious and inaccessible because of her anger.  She cannot tolerate evil acts.  Chandika does not like evil doers and becomes terribly angry on seeing them.  She slays evil doers without mercy.  Her anger is expressed in Devi Mahatmya.  A seven-year-old girl is also known as Chandika in Sanskrit scriptures.

Shakti: In Hinduism, Shakti (Devanagari: शक्ति; from Sanskrit "shak", "to be able", meaning "power" or "empowerment"), also spelled as Sakthi, is the primordial cosmic energy and represents the dynamic forces that are thought to move through the entire universe.  Shakti is the concept or personification of divine feminine creative power, sometimes referred to as 'The Great Divine Mother' in Hinduism.  As the mother she is known as Adi Parashakti or Adishakti.  On the earthly plane, Shakti most actively manifests through female embodiment and creativity/fertility, though it is also present in males in its potential, unmanifest form.

Mahakali: Mahakali (Sanskrit: Mahākālī, Devanagari: महाकाली), literally translated as "Great Kali", is the Hindu Goddess of time and death, considered to be the consort of Mahakala the God of consciousness, the basis of Reality and existence.  Mahakali in Sanskrit is etymologically the feminized variant of Mahakala or "Great Time" (which is interpreted also as "Death"), an epithet of the God Shiva in Hinduism.  Mahakali is the form of Adi parashakti, who is beyond time and space.  Kali is the force of anger of Adi parashakti and therefore her color is black.  She is the greatest aspect of Kali whom many Hindus hold as a Divine Mother.

Sati (Hindu goddess): Satī (ˈsʌti: ) (Sanskrit: सती ), is also known as Dākṣāyaṇī (Sanskrit: दाक्षायणी, lit.  "daughter of Daksha").  In the Tamil tradition, Sati is called Tamil: தாட்சாயிணி "Tāṭcāyiṇi", and in Telugu tradition she is known as Perantalu.  Sati is the goddess of marital felicity and longevity in Hinduism.  An aspect of Adi Parashakti, Dakshayani is the first consort of Shiva, the second being Parvati who is the reincarnation of Sati.

Question: In what language is the text that states that Adi Parashakti is the original creator?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "text_name": {
      "type": "string",
      "description": "The name of the Hindu text."
    },
    "language": {
      "type": "string",
      "description": "The language in which the text is written."
    },
    "deity_described": {
      "type": "string",
      "description": "The deity whose attributes or actions are described in the text."
    },
    "attribute_described": {
      "type": "string",
      "description": "The specific attribute or role of the deity mentioned in the text."
    }
  },
  "required": [
    "text_name",
    "language",
    "deity_described",
    "attribute_described"
  ],
  "additionalProperties": false
}
