#import individual examples
from Thunderbird import CreateNewMessagesToThunderbird, GetCurrentMessageSize, GetNumberOfItemsFromMBox, ReadMessagesFromThunderbird
from IMAP import AppendMessageToFolder,BuildingComplexQueries,CaseSensitiveEmailsFiltering,CopyMessageToAnotherFolder,DeleteMultipleMessages,DeleteSingleMessage,FetchEmailMessageFromServer,FilteringMessagesFromIMAPMailbox,GetMessagesWithSpecificCriterion,GettingFoldersInformation,ListingMessagesRecursively,ListingMessagesWithPagingSupport,ListingMIMEMessageIdInImapMessageInfo,MoveMessageToAnotherFolder,RetreiveExtraParametersAsSummaryInformation,RetrievingServerExtensions,SavingMessageFromIMAPServer,SetCustomFlags,SettingMessageFlags,SSLEnabledIMAPServer
from POP3 import ConnectingToPOP3,DeleteEmailByIndex,FilterMessagesFromMailbox,GetEmailCountInMailbox,GettingMailboxInfo,ListingServerExtensions,RetrieveMessageSummaryInformationUsingUniqueId,RetrievingEmailHeaders,RetrievingEmailMessages,SaveToDiscWithoutParsing,SSLEnabledPOP3Server
from SMTP import ForwardEmail,RetrieveSMTPServerExtensions,SendEmailSynchronously,SendingBulkEmails,SendingMeetingRequestsViaEmail,SendingPlainTextMessage,SendMsgAsTNEF,SetAlternateText,SettingHTMLBody,SSLEnabledSMTPServer
from WorkingWithAppointments import CreateAppointment,CreateAppointmentFromString,DraftAppointmentRequest,LoadAppointment,ReadMultipleEventsFromICS,SetParticipantStatusOfAppointmentAttendees,WriteMultipleEventsToICS
from WorkingWithMimeMessages import AddEmailAttachments,ChangeEmailAddress,CreateNewMailMesssage,DetermineAttachmendEmbeddedMessage,DisplayAttachmentFileName,DisplayEmailInformation,ExtractEmbeddedObjectsFromEmail,ExtractingEmailHeaders,GetDecodedHeaderValues,RemoveLRTracesFromMessageBody,RemovingAttachmentFromMailMessage,RetrievContentDescriptionFromAttachment,SpecifyRecipientAddresses
from WorkingWithOutlookMSGs import AddAudioReminderToCalendar,AddDisplayReminderToCalendar,AddingMSGAttachments,AddingVotingButtonToExistingMessage,AddRecurrenceToMapiTask,AddReminderInformationToMapiTask,ConvertMSGToMimeMessage,CreateAndSaveCalendarItems,CreateAndSaveOutlookContact,CreateAndSaveOutlookNote,CreatingAndSavingOutlookMSG,CreatingAndSavingOutlookTask,CreatingMSGFilesWithRtfBody,DeleteVotingButtonFromMessage,DisplayReceipientsStatusFromMeetingReqeust,GetAttachmentsFromCalendar,GetMapiProperty,LoadingContactFromMSG,LoadingContactFromVCardWithSpecifiedEncoding,LoadingContactFromVCF,LoadMsgFiles,PreservingEmbeddedMsgFormat,ReadingMapiNote,ReadingOnlyVotingButtons,ReadingVotingOptions,ReadVoteResultsInformation,RenderingContactInformationToMhtml,SaveMSGAsTemplate,SavingMessageInDraftStatus,SetBodyCompression,SetMapiProperties
from WorkingWithOutlookStorageFiles import AccessContactInformation,AddFilesToPST,AddMapiCalendarToPST,AddMapiNoteToPST,AddMapiTaskToPST,AddMessagesFromOtherPST,AddMessagesToPSTFiles,ChangeFolderContainerClass,ConvertingOSTToPST,CreateDistributionListInPST,CreateNewMapiContactsAndAddToContactsSubFolder,CreateNewMapiJournalAndAddToPST,CreateNewPSTFileAndAddingSubfolders,DeleteBulkItemsFromPst,DeleteMessagesFromPSTFile,DisplayInformationOfPSTFile,ExtractNumberOfMessages,GetMessagesInformation,MoveItemsToOtherFolders,ReadingOSTFiles,RetrievingParentFolderInformationFromMessageInfo,SaveCalendarItems,SearchingStringInPSTWithIgnoreCaseParameter,UpdateBulkMessagesInPSTFile

###################################
#Uncomment any of the following for testing
###################################

###### IMAP
#AppendMessageToFolder.run()
##BuildingComplexQueries.run()
##CaseSensitiveEmailsFiltering.run()
##CopyMessageToAnotherFolder.run()
##DeleteMultipleMessages.run()
##DeleteSingleMessage.run()
##FetchEmailMessageFromServer.run()
##FilteringMessagesFromIMAPMailbox.run()
##GetMessagesWithSpecificCriterion.run()
##GettingFoldersInformation.run()
##ListingMessagesRecursively.run()
##ListingMessagesWithPagingSupport.run()
##ListingMIMEMessageIdInImapMessageInfo.run()
##MoveMessageToAnotherFolder.run()
##RetreiveExtraParametersAsSummaryInformation.run()
##RetrievingServerExtensions.run()
##SavingMessageFromIMAPServer.run()
##SetCustomFlags.run()
##SettingMessageFlags.run()
##SSLEnabledIMAPServer.run()

###### POP3
##ConnectingToPOP3.run()
##DeleteEmailByIndex.run()
##FilterMessagesFromMailbox.run()
##GetEmailCountInMailbox.run()
##GettingMailboxInfo.run()
##ListingServerExtensions.run()
##RetrieveMessageSummaryInformationUsingUniqueId.run()
##RetrievingEmailHeaders.run()
##RetrievingEmailMessages.run()
##SaveToDiscWithoutParsing.run()
##SSLEnabledPOP3Server.run()

###### SMTP 
##ForwardEmail.run()
##RetrieveSMTPServerExtensions.run()
##SendEmailSynchronously.run()
##SendingBulkEmails.run()
##SendingMeetingRequestsViaEmail.run()
##SendingPlainTextMessage.run()
##SendMsgAsTNEF.run()
##SetAlternateText.run()
##SettingHTMLBody.run()
##SSLEnabledSMTPServer.run()

###### Thunderbird
##CreateNewMessagesToThunderbird.run()
##GetCurrentMessageSize.run()
##GetNumberOfItemsFromMBox.run()
##ReadMessagesFromThunderbird.run()

###### Working with Appointments
##CreateAppointment.run()
##CreateAppointmentFromString.run()
##DraftAppointmentRequest.run()
##LoadAppointment.run()
##ReadMultipleEventsFromICS.run()
##SetParticipantStatusOfAppointmentAttendees.run()
##WriteMultipleEventsToICS.run()

###### Working with MIME Messages
##AddEmailAttachments.run()
##ChangeEmailAddress.run()
##CreateNewMailMesssage.run()
##DetermineAttachmendEmbeddedMessage.run()
##DisplayAttachmentFileName.run()
##DisplayEmailInformation.run()
##ExtractEmbeddedObjectsFromEmail.run()
##ExtractingEmailHeaders.run()
##GetDecodedHeaderValues.run()
##RemoveLRTracesFromMessageBody.run()
##RemovingAttachmentFromMailMessage.run()
##RetrievContentDescriptionFromAttachment.run()
##SpecifyRecipientAddresses.run()

###### Working with Outlook Messages
##AddAudioReminderToCalendar.run()
##AddDisplayReminderToCalendar.run()
##AddingMSGAttachments.run()
##AddingVotingButtonToExistingMessage.run()
##AddRecurrenceToMapiTask.run()
##AddReminderInformationToMapiTask.run()
##ConvertMSGToMimeMessage.run()
##CreateAndSaveCalendarItems.run()
##CreateAndSaveOutlookContact.run()
##CreateAndSaveOutlookNote.run()
##CreatingAndSavingOutlookMSG.run()
##CreatingAndSavingOutlookTask.run()
##CreatingMSGFilesWithRtfBody.run()
##DeleteVotingButtonFromMessage.run()
##DisplayReceipientsStatusFromMeetingReqeust.run()
##GetAttachmentsFromCalendar.run()
##GetMapiProperty.run()
##LoadingContactFromMSG.run()
##LoadingContactFromVCardWithSpecifiedEncoding.run()
##LoadingContactFromVCF.run()
##LoadMsgFiles.run()
##PreservingEmbeddedMsgFormat.run()
##ReadingMapiNote.run()
##ReadingOnlyVotingButtons.run()
##ReadingVotingOptions.run()
##ReadVoteResultsInformation.run()
##RenderingContactInformationToMhtml.run()
##SaveMSGAsTemplate.run()
##SavingMessageInDraftStatus.run()
##SetBodyCompression.run()
##SetMapiProperties.run()

###### Working with Outlook Storage Files
##AccessContactInformation.run()
##AddFilesToPST.run()
##AddMapiCalendarToPST.run()
##AddMapiNoteToPST.run()
##AddMapiTaskToPST.run()
##AddMessagesFromOtherPST.run()
##AddMessagesToPSTFiles.run()
##ChangeFolderContainerClass.run()
##ConvertingOSTToPST.run()
##CreateDistributionListInPST.run()
##CreateNewMapiContactsAndAddToContactsSubFolder.run()
##CreateNewMapiJournalAndAddToPST.run()
##CreateNewPSTFileAndAddingSubfolders.run()
##DeleteBulkItemsFromPst.run()
##DeleteMessagesFromPSTFile.run()
##DisplayInformationOfPSTFile.run()
##ExtractNumberOfMessages.run()
##GetMessagesInformation.run()
##MoveItemsToOtherFolders.run()
##ReadingOSTFiles.run()
##RetrievingParentFolderInformationFromMessageInfo.run()
##SaveCalendarItems.run()
##SearchingStringInPSTWithIgnoreCaseParameter.run()
##UpdateBulkMessagesInPSTFile.run()
