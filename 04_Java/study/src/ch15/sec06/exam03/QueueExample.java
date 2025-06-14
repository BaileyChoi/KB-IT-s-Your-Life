package ch15.sec06.exam03;

import ch15.sec06.exam03.command.Command;
import ch15.sec06.exam03.command.SendKakaotalkCommand;
import ch15.sec06.exam03.command.SendMailCommand;
import ch15.sec06.exam03.command.SendSMSCommand;

import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

public class QueueExample {
    public static void main(String[] args) {
        //Queue 컬렉션 생성
        Queue<Message> messageQueue = new LinkedList<>();

        //Command Map 생성
        Map<String, Command> commands = new LinkedHashMap<>();
        commands.put("sendMail", new SendMailCommand());
        commands.put("sendSMS", new SendSMSCommand());
        commands.put("sendKakaotalk", new SendKakaotalkCommand());

        //메시지 넣기
        messageQueue.offer(new Message("sendMail", "Hong"));
        messageQueue.offer(new Message("sendSMS", "Sin"));
        messageQueue.offer(new Message("sendKakaotalk", "Gam"));

        while (!messageQueue.isEmpty()) {
            Message message = messageQueue.poll();

            // Command 호출
            Command command = commands.get(message.command);
            if (command != null) {
                command.execute(message);
            }
        }
    }
}
