package org.scoula.travel.dao;

import org.scoula.travel.domain.TravelVO;
import org.scoula.travel.domain.TravelImageVO;

import java.util.List;
import java.util.Optional;

public interface TravelDao {
    void insert(TravelVO travel);           // TravelVO를 테이블에 저장

    void insertImage(TravelImageVO image);  // TravelImageVO를 테이블에 저장

    int getTotalCount();    // 전체 데이터 건수 얻기

    List<String> getDistricts();            // 권역 목록 얻기

    List<TravelVO> getTravels();            // 전체 목록 얻기

    List<TravelVO> getTravels(int page);    // 페이지별 목록 얻기

    List<TravelVO> getTravels(String district); // 특정 권역의 목록 얻기

    Optional<TravelVO> getTravel(Long no);  // 특정 관광지 정보 얻기
}
