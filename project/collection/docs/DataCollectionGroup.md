
# Class: DataCollectionGroup



URI: [cosmos_collection:DataCollectionGroup](https://www.cdisc.org/cosmos/collection_v1.0DataCollectionGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DataCollectionItem],[DataCollectionItem]<items%201..*-++[DataCollectionGroup&#124;packageDate:date;packageType:PackageTypeEnum;collectionSpecializationId:string;shortName:string;standard:string;standardStartVersion:string;standardEndVersion:string%20%3F;domain:string%20%3F;biomedicalConceptId:string%20%3F;sdtmDatasetSpecializationId:string])](https://yuml.me/diagram/nofunky;dir:TB/class/[DataCollectionItem],[DataCollectionItem]<items%201..*-++[DataCollectionGroup&#124;packageDate:date;packageType:PackageTypeEnum;collectionSpecializationId:string;shortName:string;standard:string;standardStartVersion:string;standardEndVersion:string%20%3F;domain:string%20%3F;biomedicalConceptId:string%20%3F;sdtmDatasetSpecializationId:string])

## Attributes


### Own

 * [packageDate](packageDate.md)  <sub>1..1</sub>
     * Description: Biomedical Concept package release date indicating when the BC package was published to production
     * Range: [Date](types/Date.md)
 * [packageType](packageType.md)  <sub>1..1</sub>
     * Description: Package type for data collection specializations (collection)
     * Range: [PackageTypeEnum](PackageTypeEnum.md)
 * [collectionSpecializationId](collectionSpecializationId.md)  <sub>1..1</sub>
     * Description: Identifier for data collection specialization group
     * Range: [String](types/String.md)
 * [shortName](shortName.md)  <sub>1..1</sub>
     * Description: Short name which provides a user friendly and intuitive name for the data collection group
     * Range: [String](types/String.md)
 * [standard](standard.md)  <sub>1..1</sub>
     * Description: Standard for the data collection specialization group
     * Range: [String](types/String.md)
 * [standardStartVersion](standardStartVersion.md)  <sub>1..1</sub>
     * Description: The earliest data collection IG version applicable to the collection specialization
     * Range: [String](types/String.md)
 * [standardEndVersion](standardEndVersion.md)  <sub>0..1</sub>
     * Description: The last data collection IG version that is applicable to the collection specialization
     * Range: [String](types/String.md)
 * [domain](domain.md)  <sub>0..1</sub>
     * Description: Domain for the data collection specialization group
     * Range: [String](types/String.md)
 * [biomedicalConceptId](biomedicalConceptId.md)  <sub>0..1</sub>
     * Description: Biomedical Concept identifier foreign key
     * Range: [String](types/String.md)
 * [sdtmDatasetSpecializationId](sdtmDatasetSpecializationId.md)  <sub>1..1</sub>
     * Description: Identifier for SDTM Dataset Specialization group
     * Range: [String](types/String.md)
 * [items](items.md)  <sub>1..\*</sub>
     * Description: Item included in the Data Collection dataset specialization
     * Range: [DataCollectionItem](DataCollectionItem.md)
