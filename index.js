exports.handler = async (event, context) => {
  try {
    const sqsRecords = event.Records;

    for (const record of sqsRecords) {
      const messageBody = JSON.parse(record.body);

      await processMessage(messageBody);
    }

    return {
      statusCode: 200,
      body: 'Message processing completed'
    };
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
};

async function processMessage(messageBody) {
  // Implement your custom logic to process the message body
  console.log('Received message body:', messageBody);
}
