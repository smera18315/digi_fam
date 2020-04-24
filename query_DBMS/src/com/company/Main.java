package com.company;
import javax.xml.transform.Result;
import java.sql.*;

public class Main {

    public static String get_id(){
        return "5";
    }
    public static String get_date(){
        return "2020-04-25";
    }

    public static void main(String[] args) {
        String service ="Amazon Prime";
        String handle ="44-340-1384";
        String number = "9192939495";
        String person_id ="10";
        String event_id ="5";
	// write your code here
        try{
            Class.forName("com.mysql.jdbc.Driver");
            Connection con=DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/digifam?useSSL=false","root","Banger2170@3");
            Statement stmt=con.createStatement();
            String sql1 = "Select V.person_id from subscription U inner join subscription V where U.person_id!=V.person_id and U.person_id=\"39\" and U.subscription_service=\"NETFLIX\" and U.account_id = V.account_id;";
            String sql2 = "Select * from event E where E.Organiser_id = \"41\" and date between '2020-01-01' and '2020-12-31';";
            String sql3 = "SELECT U.Person_id, U.Name " + "FROM User_data as U, School as S " + "WHERE U.person_id = S.person_id AND S.C"+"lass = \"12\" AND S.School = \"Basilicata University Potenza\";";
            String sql4 ="Select v.event_id,v.event_folder_URL from event u inner join family_folder v where u.event_id = v.event_id and u.organiser_name=\"Quinn Didsbury\" and u.date > '2019-12-31' and u.date < '2021-01-01';";
            String sql5 ="SELECT U.person_id, U.Name " +
                    " FROM user_data as U, medical_sercives as M " +
                    " WHERE U.person_id = M.person_id AND " +
                    " M.Disease = \"Dengue\" AND M.checkup_date = '2020-12-05';";
            String sql6 ="SELECT C.user_id,U.Name " +
                    "FROM Calender_event as C, user_data as U " +
                    "WHERE C.event_type = 'Wedding' AND C.going = '1' AND " +
                    " C.user_id =U.person_id AND YEAR(C.date) = '2020';";
            String sql7 ="SELECT SUM(total_fees) " +
                    " from medical_sercives " +
                    " where Person_id = \"5\" and checkup_date between '2019-01-01' and '2020-12-31';";
            String sql8 ="SELECT * from event where Organiser_Id = \"25\" and month(date) = '01' and day(date) = '01'; ";
            String sql10 = "SELECT distinct M.Disease " +
                    "    FROM medical_sercives as M " +
                    "    Where year(checkup_date) = '2020';";
            String sql9 ="SELECT E.Organiser_name " +
                    "        FROM Event as E " +
                    "        WHERE E.date = '2020-04-02';";
            String sql11 = "SELECT v.name from relation r left join user_data v on r.user_2_id = v.person_id where  r.user_1_id =\""+get_id()+"\" ORDER by priority LIMIT 5;";
            String sql12 = "SELECT * from insurance I where DATE_ADD(I.policy_taken_date, INTERVAL I.policy_term YEAR)<=DATE_ADD('"+get_date()+"',INTERVAL 6 MONTH) ;";
            String sql13 = "SELECT person_id from user_data U where day(U.birthday) =day('"+ get_date() + "') AND month(U.birthday) = month('"+ get_date() + "')";
            String sql14 = "DELETE from Subscription WHERE Subscription_Service = '" + service + "' AND Account_id = \"" + handle + "\"";
            String sql15 = "UPDATE User_Data set contact_no = \"" + (number) + "\" WHERE Person_id = \"" + person_id+ "\"" ;
            String sql16 = "Insert into event_id_people_invited values(\"" +event_id+ "\", \"" +person_id+ "\")";
            String sql17 = "SELECT count(*) from Calender_Event WHERE event_type = \"Birthday\" AND Priority <= 4 AND MONTH('"+get_date()+"')= MONTH(date);";
            String sql18 = "UPDATE User_data set premium = \"1\" , validity = DATE_ADD('"+get_date()+"', INTERVAL 1 YEAR) WHERE Person_id =\"5\"";

            ResultSet rs=stmt.executeQuery(sql1);
            System.out.println("Answer for query :\n"+ sql1+"\n");
            while(rs.next()) {

                System.out.println(rs.getString(1));
            }
            rs=stmt.executeQuery(sql2);
            System.out.println("Answer for query :\n"+ sql2+"\n");
            while(rs.next()) {

                System.out.println(rs.getString(1)+"  "+rs.getString(2)+"  "+rs.getString(3)+"  "+rs.getString(4)+"  "+rs.getString(5)+"  "+rs.getString(6)+"  "+rs.getString(7)+"  "+rs.getString(8));

            }
            rs=stmt.executeQuery(sql3);
            System.out.println("Answer for query :\n"+ sql3+"\n");
            while(rs.next()) {

                System.out.println(rs.getString(1)+"  "+rs.getString(2));
            }
            rs=stmt.executeQuery(sql4);
            System.out.println("Answer for query :\n"+ sql4+"\n");
            while(rs.next()) {

                System.out.println(rs.getString(1)+"  "+rs.getString(2));
            }
            rs=stmt.executeQuery(sql5);
            System.out.println("Answer for query :\n"+ sql5+"\n");
            while(rs.next()) {

                System.out.println(rs.getString(1)+"  "+rs.getString(2));
            }
            rs=stmt.executeQuery(sql6);
            System.out.println("Answer for query :\n"+ sql6+"\n");
            while(rs.next()) {

                System.out.println(rs.getString(1)+"  "+rs.getString(2));
            }
            rs=stmt.executeQuery(sql7);
            System.out.println("Answer for query :\n"+ sql7+"\n");
            while(rs.next()) {

                System.out.println(rs.getString(1));
            }
            rs=stmt.executeQuery(sql8);
            System.out.println("Answer for query :\n"+ sql8+"\n");
            while(rs.next()) {

                System.out.println(rs.getString(1)+"  "+rs.getString(2)+"  "+rs.getString(3)+"  "+rs.getString(4)+"  "+rs.getString(5)+"  "+rs.getString(6)+"  "+rs.getString(7)+"  "+rs.getString(8));
            }
            rs=stmt.executeQuery(sql9);
            System.out.println("Answer for query :\n"+ sql9+"\n");
            while(rs.next()) {

                System.out.println(rs.getString(1));
            }
            rs=stmt.executeQuery(sql10);
            System.out.println("Answer for query :\n"+ sql10+"\n");
            while(rs.next()) {

                System.out.println(rs.getString(1));
            }
            rs=stmt.executeQuery(sql11);
            System.out.println("Answer for query :\n"+ sql11+"\n");
            while(rs.next()) {

                System.out.println(rs.getString(1));
            }
            rs=stmt.executeQuery(sql12);
            System.out.println("Answer for query :\n"+ sql12+"\n");
            while(rs.next()) {

                System.out.println(rs.getString(1)+"  "+rs.getString(2)+"  "+rs.getString(3)+"  "+rs.getString(4)+"  "+rs.getString(5)+"  "+rs.getString(6)+"  "+rs.getString(7));
            }
            rs=stmt.executeQuery(sql13);
            System.out.println("Answer for query :\n"+ sql13+"\n");
            System.out.println("happy birthday");
            while(rs.next()) {

                System.out.println(rs.getString(1));
            }
            int r=stmt.executeUpdate(sql14);
            System.out.println("Answer for query :\n"+ sql14+"\n");
            if(r==1){

                System.out.println("success");
            }
            r=stmt.executeUpdate(sql15);
            System.out.println("Answer for query :\n"+ sql15+"\n");
            if(r==1){

                System.out.println("success");
            }
            r=stmt.executeUpdate(sql16);
            System.out.println("Answer for query :\n"+ sql16+"\n");
            if(r==1){

                System.out.println("success");
            }
            rs=stmt.executeQuery(sql17);
            System.out.println("Answer for query :\n"+ sql17+"\n");
            while(rs.next()) {

                System.out.println(rs.getString(1));
            }
            r=stmt.executeUpdate(sql18);
            System.out.println("Answer for query :\n"+ sql18+"\n");
            if(r==1){

                System.out.println("success");
            }


            con.close();
        }catch(Exception e){ System.out.println(e);}
    }
}

